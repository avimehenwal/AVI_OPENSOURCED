use std::env;

struct TodoItem {
    name: String,
    completed: char
}

impl TodoItem {
    fn new(name: String) -> TodoItem {
        return TodoItem{
            name: name,
            completed: ' '
        };
    }
}

fn main() {
    let arguments: Vec<String> = env::args().collect();
    let command = &arguments[1];    // borrow

    let todo_item = TodoItem{
        name: "Avi Mehenwal".to_string(),
        completed: ' '
    };
    let todo_item_2 = TodoItem::new("Say Hi".to_string());
    let todo_item_3 = TodoItem::new("To Me".to_string());

    let todo_list = vec![todo_item, todo_item_2, todo_item_3];

    println!("{:#?}", command);
    if command == "get" {
        println!("We got a get");
        for item in todo_list {
            println!("[{}] - {}", item.completed, item.name)
        }
    }

}
