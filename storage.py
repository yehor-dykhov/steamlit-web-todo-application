STORAGE_FILE = 'todos.txt'
SEPARATOR = '<:::>'


def save_todos(todos):
    with open(STORAGE_FILE, 'w') as file:
        for id, title in todos:
            file.writelines(f"{id}{SEPARATOR}{title}" + '\n')


def get_todos():
    todos = []

    with open(STORAGE_FILE) as file:
        for line in file:
            if line != '':
                todos.append(line.strip().split(SEPARATOR))

    return todos


def init_storage():
    try:
        with open(STORAGE_FILE) as _:
            _
    except FileNotFoundError:
        with open(STORAGE_FILE, 'w') as _:
            _
