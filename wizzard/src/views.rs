use inquire::{error::InquireResult, Select};

use crate::models::Models;

mod list;
mod show;

fn actions() -> Vec<&'static str> {
    vec!["list", "show", "install", "uninstall", "exit"]
}

pub fn run(models: &Models) -> InquireResult<()> {
    loop {
        let action = Select::new("Action:", actions()).prompt()?;

        match action {
            "list" => list::handle(models),
            "show" => show::handle(models)?,
            "exit" => break,
            _ => {}
        }
    }
    Ok(())
}
