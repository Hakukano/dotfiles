mod models;
mod services;

fn main() {
    let service = services::instantiate();

    println!("Hello, world!");
}
