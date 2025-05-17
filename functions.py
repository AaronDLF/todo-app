FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
  """Read a text file and return the list of to-do items.
  Each line in the file is a separate to-do item."""
  with open(filepath, 'r') as file_local:
    todos_local = file_local.readlines()
  return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
  """Write the to-do items list in the text file."""
  with open(filepath, 'w') as file_local:
    file_local.writelines(todos_arg)


if __name__ == "__main__":
  print("This program is not meant to be run directly.")
  print("Please use the main.py file to run the program.")
  exit(0)