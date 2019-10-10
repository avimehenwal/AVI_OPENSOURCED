use std::env;


fn main() {
    let args: Vec<String> = env::args().collect();

    let x = &args[1];
    let y = &args[2];

    //println!("{} / {} = {}", x, y, x/y);
    println!("Args = {} {}", x, y);
}
