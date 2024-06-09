prompt = "Type 'add', 'show', 'edit', 'complete' or 'exit' : "

todos = []

while(True):
    user_action = input(prompt).strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ").strip()
            todos.append(todo.capitalize())
        case 'show':
           for (index, item) in enumerate(todos):
               print(f"{index+1}-{item}")
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number -=1
            exisitng_todo = todos[number]
            print(exisitng_todo)
            new_todo = input("Enter the todo: ").strip()
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of todo to complete: "))
            number -=1
            todos.pop(number)
        case 'exit':
            break

print("Bye")

    

