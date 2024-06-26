use std::{
    fs,
    os::unix::fs::symlink,
    path::{Path, PathBuf},
};

use anyhow::Result;
use serde::Deserialize;

#[derive(Clone, Debug, Deserialize)]
pub struct Config {
    description: String,
    src: String,
    dst: String,
}

impl Config {
    pub fn description(&self) -> &str {
        self.description.as_str()
    }

    pub fn absolute_src(&self) -> PathBuf {
        fs::canonicalize(Path::new(
            shellexpand::env(self.src.as_str())
                .expect("Cannot expand src path")
                .as_ref(),
        ))
        .expect("Cannot get absolute path of src")
    }

    pub fn absolute_dst(&self) -> PathBuf {
        Path::new(
            shellexpand::env(self.dst.as_str())
                .expect("Cannot expand dst path")
                .as_ref(),
        )
        .to_path_buf()
    }

    pub fn linked(&self) -> bool {
        let path = self.absolute_dst();
        if !path.is_symlink() {
            return false;
        }
        if let Ok(src) = fs::read_link(path) {
            src == self.absolute_src()
        } else {
            false
        }
    }

    pub fn link(&self) -> Result<()> {
        symlink(self.absolute_src(), self.absolute_dst()).map_err(Into::into)
    }

    pub fn unlink(&self) -> Result<()> {
        fs::remove_file(self.absolute_dst()).map_err(Into::into)
    }
}
