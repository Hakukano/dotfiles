use serde::Deserialize;

use super::cmd::Cmd;

#[derive(Clone, Debug, Deserialize)]
pub struct Check(Cmd);

impl Check {
    pub fn ok(&self) -> bool {
        self.0.status_no_output().success()
    }
}
