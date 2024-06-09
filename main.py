prompt = "Type 'add', 'show', 'edit' or 'exit' : "

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
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number -=1
            exisitng_todo = todos[number]
            print(exisitng_todo)
            new_todo = input("Enter the todo: ").strip()
            todos[number] = new_todo
        case 'exit':
            break

print("Bye")

    

