prompt = "Type 'add', 'show' or 'exit' : "

todos = []

while(True):
    user_action = input(prompt)
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())            
        case 'show':
            print(todos)
        case 'exit':
            break
    

