fn main() {
    println!("Hello, world!");
    use std::env;

    let arguments: Vec<String> = env::args().collect();
    let command = &arguments[1];
    let args = &arguments[2];

    println!("{:#?}", command);
    println!("{:#?}", args);

}
