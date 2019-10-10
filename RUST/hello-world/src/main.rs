fn main() {
    println!("Hello, world!");
    http_req();
}

fn http_req() {
    let body = reqwest::get('https://www.rust-lang.org')?
        .text()?;
    println!("body = {:?}", body);
}