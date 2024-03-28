use std::process::{Command, ExitStatus};

use serde::Deserialize;

macro_rules! gen_command {
    ($self:ident) => {
        Command::new($self.0.first().expect("No binary name found")).args($self.0.iter().skip(1))
    };
}

#[derive(Clone, Deserialize)]
pub struct Cmd(Vec<String>);

impl Cmd {
    pub fn command(&self) -> String {
        self.0.join(" ")
    }

    pub fn status(&self) -> ExitStatus {
        gen_command!(self).status().expect("Cannot get status")
    }
}
