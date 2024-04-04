use prettytable::{color, Attr, Cell, Row, Table};

use crate::models::Models;

pub fn handle(models: &Models) {
    let mut table = Table::new();
    table.add_row(Row::new(vec![
        Cell::new("Name").with_style(Attr::Bold),
        Cell::new("Description").with_style(Attr::Bold),
        Cell::new("Installed").with_style(Attr::Bold),
    ]));
    for (name, model) in models.iter() {
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
}
