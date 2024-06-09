prompt = "Type 'add', 'show' or 'exit' : "

todos = []

while(True):
    user_action = input(prompt).strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ").strip()
            todos.append(todo.capitalize())            
        case 'show':
           for item in todos:
               print(item)
        case 'exit':
            break
    

