use std::io;

use crossterm::{execute, style::Print};
use inquire::{error::InquireResult, Select};

use crate::models::Models;

mod install;
mod list;
mod show;
mod uninstall;

fn actions() -> Vec<&'static str> {
    vec!["list", "show", "install", "uninstall", "exit"]
}

pub fn run(models: &Models) -> InquireResult<()> {
    loop {
        let action = Select::new("Action:", actions()).prompt()?;

        execute!(io::stdout(), Print("\n"))?;

        match action {
            "list" => list::handle(models),
            "show" => show::handle(models)?,
            "install" => install::handle(models)?,
            "uninstall" => uninstall::handle(models)?,
            "exit" => break,
            _ => {}
        }

        execute!(io::stdout(), Print("\n"))?;
    }
    Ok(())
}
