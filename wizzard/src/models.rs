use std::{
    collections::{HashMap, HashSet},
    env,
    fs::{self, File},
    ops::Deref,
};

use anyhow::Result;
use json_value_merge::Merge;
use serde::Deserialize;
use serde_json::{json, Value};
use tap::{Pipe, Tap};

mod check;
mod cmd;
mod config;
mod install;

use check::Check;
use config::Config;
use install::Install;

#[derive(Clone, Deserialize)]
pub struct Model {
    description: String,
    check: Check,
    #[serde(default)]
    dependencies: Vec<String>,
    #[serde(default)]
    configs: HashMap<String, Config>,
    #[serde(default)]
    installs: HashMap<String, Install>,
}

impl Model {
    pub fn description(&self) -> &str {
        self.description.as_str()
    }

    pub fn check(&self) -> String {
        self.check.command()
    }

    pub fn dependencies(&self) -> &[String] {
        self.dependencies.as_slice()
    }

    pub fn configs(&self) -> &HashMap<String, Config> {
        &self.configs
    }

    pub fn installs(&self) -> &HashMap<String, Install> {
        &self.installs
    }

    pub fn installed(&self) -> bool {
        self.check.ok()
    }

    pub fn missing_dependencies(&self, installed: HashSet<String>) -> Vec<&String> {
        self.dependencies
            .iter()
            .filter(|dependency| !installed.contains(*dependency))
            .collect()
    }

    pub fn config(&self, overwrite: bool) -> Result<()> {
        self.configs
            .values()
            .filter_map(|config| {
                if overwrite || !config.linked() {
                    Some(config.link())
                } else {
                    None
                }
            })
            .collect()
    }

    pub fn install(&self, overwrite: bool) -> Result<()> {
        self.installs
            .values()
            .filter_map(|install| {
                if overwrite || !install.installed() {
                    Some(install.install())
                } else {
                    None
                }
            })
            .collect()
    }
}

#[derive(Clone)]
pub struct Models(HashMap<String, Model>);

impl Models {
    pub fn new() -> Self {
        let dist = match env::consts::OS {
            "macos" => "macos".to_string(),
            "linux" => sys_info::linux_os_release()
                .expect("Cannot get linux os release")
                .id()
                .to_string(),
            dist => panic!("Unknown os: {}", dist),
        };
        Self(
            fs::read_dir("models")
                .expect("Cannot find models directory")
                .map(|entry| {
                    let path = entry.expect("Cannot find model file").path();
                    let name = path
                        .file_stem()
                        .expect("Invalid model file name")
                        .to_str()
                        .expect("Invalid model file name string")
                        .to_string();
                    let models: HashMap<String, Value> = path
                        .pipe(File::open)
                        .expect("Cannot read model file")
                        .pipe(serde_json::from_reader)
                        .expect("Cannot parse model file");
                    let model = models
                        .get("default")
                        .cloned()
                        .unwrap_or_else(|| json!({}))
                        .tap_mut(|value| {
                            value.merge(&models.get(&dist).cloned().unwrap_or_else(|| json!({})))
                        })
                        .pipe(serde_json::from_value)
                        .expect("Invalid model structure");
                    (name, model)
                })
                .collect(),
        )
    }

    pub fn installed(&self) -> HashSet<String> {
        self.iter()
            .filter_map(|(k, v)| if v.installed() { Some(k.clone()) } else { None })
            .collect()
    }
}

impl Deref for Models {
    type Target = HashMap<String, Model>;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}
