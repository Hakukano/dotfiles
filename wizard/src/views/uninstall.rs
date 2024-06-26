use std::io;

use crossterm::{
    execute,
    style::{Color, Print, ResetColor, SetForegroundColor},
};
use inquire::{error::InquireResult, Confirm, Select};

use crate::models::Models;

pub fn handle(models: &Models) -> InquireResult<()> {
    let model_name = Select::new("Model:", models.keys().collect()).prompt()?;
    execute!(io::stdout(), Print("\n"))?;

    let dependents = models.installed_dependents(model_name);
    if !dependents.is_empty() {
        execute!(
            io::stderr(),
            SetForegroundColor(Color::Red),
            Print(format!(
                "These dependents are still installed, please uninstall them first: {}\n",
                dependents.join(", ")
            )),
            ResetColor
        )?;
        return Ok(());
    }

    let model = models.get(model_name);
    if let Some(model) = model {
        if !model.installed() {
            execute!(
                io::stdout(),
                SetForegroundColor(Color::Yellow),
                Print(format!(
                    "{} is not installed, skipping\n",
                    model.description()
                )),
                ResetColor,
            )?;
            return Ok(());
        }

        if Confirm::new("Uninstall this model?")
            .with_default(false)
            .prompt()?
        {
            execute!(
                io::stdout(),
                SetForegroundColor(Color::Yellow),
                Print(format!("\nUninstalling {}\n", model.description())),
                ResetColor
            )?;
            if let Err(err) = model.uninstall() {
                execute!(
                    io::stderr(),
                    SetForegroundColor(Color::Red),
                    Print(format!(
                        "Cannot uninstall {}: {}\n",
                        model.description(),
                        err
                    )),
                    ResetColor
                )?;
            }
        }
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
