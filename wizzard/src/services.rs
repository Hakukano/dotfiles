mod memory;

pub trait Service {}

pub fn instantiate() -> Box<dyn Service> {
    Box::new(memory::Service::new())
}
