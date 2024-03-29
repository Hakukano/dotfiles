use crate::models::Models;

pub struct Service {
    models: Models,
}

impl Service {
    pub fn new() -> Self {
        Self {
            models: Models::new(),
        }
    }
}

impl super::Service for Service {
    fn models(&self) -> &Models {
        &self.models
    }
}
