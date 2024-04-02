use inquire::{error::InquireResult, Select};

use crate::models::Models;

pub fn handle(models: &Models) -> InquireResult<()> {
    let model = Select::new("Model:", models.keys().collect()).prompt()?;
    Ok(())
}
