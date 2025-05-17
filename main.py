import functions
import time

print("This is the current date and time:")
now = time.strftime("%d-%b-%Y %H:%M:%S")
print("It is", now)
print("Welcome to your todo app!")
while True:
  user_action = input("Type add, show, edit, complete or exit:")

  if user_action.startswith("add"):
    todo = user_action[4:] + "\n"

    todos = functions.get_todos()

    todos.append(todo)

    functions.write_todos(todos)

  elif user_action.startswith("show"):
    todos = functions.get_todos()
    #the list comprehension below is equivalent to the for loop below it

    #new_todos = [item.strip("\n") for item in todos]

    for index, item in enumerate(todos):
      item = item.strip("\n")
      row = f"{index + 1}.{item}"
      print(row)

  elif user_action.startswith("edit"):
    try:
      number = int(user_action[5:])
      number -= 1

      todos = functions.get_todos()

      new_todo = input("Enter the new todo: ")
      todos[number] = new_todo + "\n"

      functions.write_todos(todos)
    except ValueError:
      print("Your command is not valid. Please enter a number after 'edit'.")
      continue

  elif user_action.startswith("complete"):
    try:
      number = int(user_action[9:])

      todos = functions.get_todos()

      index = number - 1
      todo_to_remove = todos[index]
      todos.pop(index)

      functions.write_todos(todos)

      message = f"The todo '{todo_to_remove.strip("\n")}' was removed from the todo list."
      print(message)
    except IndexError:
      print("There is no item with that number.")
      continue

  elif user_action.startswith("exit") or user_action.startswith("close"):
    print("Exiting the program...")
    break

  else:
    print("Command not recognized. Please try again.")


print("Bye!")



