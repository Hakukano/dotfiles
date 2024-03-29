use serde::Deserialize;

use super::cmd::Cmd;

#[derive(Clone, Debug, Deserialize)]
pub struct Check(Cmd);

impl Check {
    pub fn command(&self) -> String {
        self.0.command()
    }

    pub fn ok(&self) -> bool {
        self.0.status().success()
    }
}
