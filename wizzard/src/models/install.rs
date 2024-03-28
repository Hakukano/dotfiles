use anyhow::{anyhow, Result};
use serde::Deserialize;

use super::{check::Check, cmd::Cmd};

#[derive(Clone, Deserialize)]
pub struct Install {
    description: String,
    check: Check,
    commands: Vec<Cmd>,
}

impl Install {
    pub fn description(&self) -> &str {
        self.description.as_str()
    }

    pub fn check(&self) -> String {
        self.check.command()
    }

    pub fn commands(&self) -> Vec<String> {
        self.commands.iter().map(Cmd::command).collect()
    }

    pub fn installed(&self) -> bool {
        self.check.ok()
    }

    pub fn install(&self) -> Result<()> {
        for command in self.commands.iter() {
            if !command.status().success() {
                return Err(anyhow!("Failed to install: {}", command.command()));
            }
        }
        Ok(())
    }
}
