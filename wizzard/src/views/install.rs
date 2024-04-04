use std::io;

use crossterm::{
    execute,
    style::{Color, Print, ResetColor, SetForegroundColor},
};
use inquire::{error::InquireResult, Confirm, Select};
use tap::Pipe;

use crate::models::{Model, Models};

fn install(model: &Model, models: &Models) -> InquireResult<()> {
    if model.installed() {
        execute!(
            io::stdout(),
            SetForegroundColor(Color::Yellow),
            Print(format!(
                "{} is already installed, skipping\n",
                model.description()
            )),
            ResetColor,
        )?;
        return Ok(());
    }

    let missing_dependencies = models.missing_dependencies(model);
    if missing_dependencies.is_empty() {
        if Confirm::new("Install this model?")
            .with_default(false)
            .prompt()?
        {
            execute!(
                io::stdout(),
                SetForegroundColor(Color::Yellow),
                Print(format!("Installing {}\n", model.description())),
                ResetColor
            )?;
            if let Err(err) = model.install() {
                execute!(
                    io::stderr(),
                    SetForegroundColor(Color::Red),
                    Print(format!("Cannot install model: {}\n\n", err)),
                    ResetColor
                )?;
            }
        }
        execute!(io::stdout(), Print("\n"))?;
    } else {
        execute!(
            io::stderr(),
            SetForegroundColor(Color::Red),
            Print(format!(
                "Missing dependency: {}\n\n",
                missing_dependencies.join(", ")
            )),
            ResetColor
        )?;
        if Confirm::new("Install all dependencies?")
            .with_default(false)
            .prompt()?
        {
            missing_dependencies
                .iter()
                .filter_map(|dep| models.get(dep.as_str()).map(|model| install(model, models)))
                .collect::<InquireResult<Vec<_>>>()?;
        }
        execute!(io::stdout(), Print("\n"))?;
    }
    Ok(())
}

pub fn handle(models: &Models) -> InquireResult<()> {
    let model = Select::new("Model:", models.keys().collect())
        .prompt()?
        .pipe(|model| models.get(model));
    execute!(io::stdout(), Print("\n"))?;
    if let Some(model) = model {
        install(model, models)?;
    } else {
        execute!(
            io::stderr(),
            SetForegroundColor(Color::Red),
            Print("Unknown model\n"),
            ResetColor
        )?;
    }
    Ok(())
}
