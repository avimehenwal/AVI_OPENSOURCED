use std::env;

struct TodoItem {
    name: String,
    completed: char
}

fn main() {
    let arguments: Vec<String> = env::args().collect();
    let command = &arguments[1];    // borrow

    let todo_item = TodoItem{
        name: "Avi Mehenwal".to_string(),
        completed: ' '
    };
    let todo_list = vec![todo_item];

    println!("{:#?}", command);
    if command == "get" {
        println!("We got a get");
        for item in todo_list {
            println!("[{}] - {}", item.completed, item.name)
        }
    }

}
