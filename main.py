from functions import get_todos, write_todos
import time


now = time.strftime("%B %d, %Y, %I:%M%p")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item = item.title()
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("Enter a new to do: ")
            (todos[number]) = new_todo + '\n'

            write_todos(todos)

        except (ValueError, IndexError):
            print("Your command is invalid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            to_do_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_todos(todos)

            message = f"Todo {to_do_remove} was removed from the list"
            print(message)
        except ValueError:
            print("Your command is invalid")
            continue
        except IndexError:
            print("That number does not exist")
            continue

    elif user_action.startswith('exit'):
        print("Goodbye!")
        break

    else:
        print("Invalid Command")
