mod models;
mod views;

fn main() {
    let models = models::Models::new();

    views::run(&models).unwrap();
}
