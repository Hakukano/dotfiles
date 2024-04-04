use std::io;

use crossterm::{
    execute,
    style::{Attribute, Color, Print, ResetColor, SetAttribute, SetForegroundColor},
};
use inquire::{error::InquireResult, Select};
use prettytable::{color, Attr, Cell, Row, Table};
use tap::Pipe;

use crate::models::{config::Config, install::Install, Model, Models};

fn print_info(model: &Model) -> InquireResult<()> {
    execute!(
        io::stdout(),
        SetAttribute(Attribute::Bold),
        Print("Description"),
        SetAttribute(Attribute::Reset),
        Print(format!(": {}\n", model.description())),
        SetAttribute(Attribute::Bold),
        Print("Installed"),
        SetAttribute(Attribute::Reset),
        Print(": "),
    )?;
    if model.installed() {
        execute!(
            io::stdout(),
            SetForegroundColor(Color::Green),
            Print("Yes\n"),
            ResetColor,
        )?;
    } else {
        execute!(
            io::stdout(),
            SetForegroundColor(Color::Red),
            Print("No\n"),
            ResetColor,
        )?;
    }
    Ok(())
}

fn print_dependencies(dependencies: &[String], models: &Models) -> InquireResult<()> {
    execute!(
        io::stdout(),
        SetAttribute(Attribute::Bold),
        Print("Dependencies"),
        SetAttribute(Attribute::Reset),
        Print(":\n"),
    )?;
    let mut table = Table::new();
    table.add_row(Row::new(vec![
        Cell::new("Name").with_style(Attr::Bold),
        Cell::new("Description").with_style(Attr::Bold),
        Cell::new("Installed").with_style(Attr::Bold),
    ]));
    for (name, model) in dependencies
        .iter()
        .filter_map(|dep| models.get(dep).map(|model| (dep, model)))
    {
        table.add_row(Row::new(vec![
            Cell::new(name),
            Cell::new(model.description()),
            if model.installed() {
                Cell::new("Yes").with_style(Attr::ForegroundColor(color::GREEN))
            } else {
                Cell::new("No").with_style(Attr::ForegroundColor(color::RED))
            },
        ]));
    }
    table.printstd();
    Ok(())
}

fn print_configs(configs: &[Config]) -> InquireResult<()> {
    execute!(
        io::stdout(),
        SetAttribute(Attribute::Bold),
        Print("Configurations"),
        SetAttribute(Attribute::Reset),
        Print(":\n"),
    )?;
    let mut table = Table::new();
    table.add_row(Row::new(vec![
        Cell::new("Description").with_style(Attr::Bold),
        Cell::new("Source").with_style(Attr::Bold),
        Cell::new("Destination").with_style(Attr::Bold),
        Cell::new("Linked").with_style(Attr::Bold),
    ]));
    for config in configs.iter() {
        table.add_row(Row::new(vec![
            Cell::new(config.description()),
            Cell::new(config.absolute_src().to_str().unwrap_or_default()),
            Cell::new(config.absolute_dst().to_str().unwrap_or_default()),
            if config.linked() {
                Cell::new("Yes").with_style(Attr::ForegroundColor(color::GREEN))
            } else {
                Cell::new("No").with_style(Attr::ForegroundColor(color::RED))
            },
        ]));
    }
    table.printstd();
    Ok(())
}

fn print_installs(installs: &[Install]) -> InquireResult<()> {
    execute!(
        io::stdout(),
        SetAttribute(Attribute::Bold),
        Print("Installations"),
        SetAttribute(Attribute::Reset),
        Print(":\n"),
    )?;
    let mut table = Table::new();
    table.add_row(Row::new(vec![
        Cell::new("Description").with_style(Attr::Bold),
        Cell::new("Installed").with_style(Attr::Bold),
    ]));
    for install in installs.iter() {
        table.add_row(Row::new(vec![
            Cell::new(install.description()),
            if install.installed() {
                Cell::new("Yes").with_style(Attr::ForegroundColor(color::GREEN))
            } else {
                Cell::new("No").with_style(Attr::ForegroundColor(color::RED))
            },
        ]));
    }
    table.printstd();
    Ok(())
}

pub fn handle(models: &Models) -> InquireResult<()> {
    let model = Select::new("Model:", models.keys().collect())
        .prompt()?
        .pipe(|model| models.get(model));
    execute!(io::stdout(), Print("\n"))?;
    if let Some(model) = model {
        print_info(model)?;
        if !model.dependencies().is_empty() {
            execute!(io::stdout(), Print("\n"))?;
            print_dependencies(model.dependencies(), models)?;
        }
        if !model.configs().is_empty() {
            execute!(io::stdout(), Print("\n"))?;
            print_configs(model.configs())?;
        }
        if !model.installs().is_empty() {
            execute!(io::stdout(), Print("\n"))?;
            print_installs(model.installs())?;
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
