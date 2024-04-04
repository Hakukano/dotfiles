use std::process::{Command, ExitStatus, Stdio};

use serde::Deserialize;

macro_rules! gen_command {
    ($self:ident) => {
        Command::new(
            shellexpand::env($self.0.first().expect("No binary name found"))
                .expect("Cannot expand command binary")
                .as_ref(),
        )
        .args($self.0.iter().skip(1).map(|arg| {
            shellexpand::env(arg)
                .expect("Cannot expand command binary")
                .to_string()
        }))
    };
}

#[derive(Clone, Debug, Deserialize)]
pub struct Cmd(Vec<String>);

impl Cmd {
    pub fn command(&self) -> String {
        self.0.join(" ")
    }

    pub fn status(&self) -> ExitStatus {
        gen_command!(self)
            .stdout(Stdio::null())
            .status()
            .expect("Cannot get status")
    }
}
