use crate::models::Models;

mod memory;

pub trait Service {
    fn models(&self) -> &Models;
}

pub fn instantiate() -> Box<dyn Service> {
    Box::new(memory::Service::new())
}
