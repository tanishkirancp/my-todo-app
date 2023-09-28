FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read the todos.txt file and returns todo items."""
    with open(filepath, 'r', encoding='utf-8') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(obj, path=FILEPATH):
    """Writes the edited todos into the default file todos.txt."""
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(obj)


if __name__ == "__main__":
    print("hi")
