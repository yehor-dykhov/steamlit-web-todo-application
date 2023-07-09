import uuid
import time
import streamlit as st
import storage

if "visibility" not in st.session_state:
    storage.init_storage()
    todos = storage.get_todos()


def handle_add_todo():
    new_todo_title = st.session_state['new_todo']
    if new_todo_title:
        todos.append((uuid.uuid4(), new_todo_title))
        storage.save_todos(todos)
        st.session_state['new_todo'] = ''
        st.success(f'"{new_todo_title}" todo was added to list!', icon="✍️")


def handle_checkbox_change(id, title, index):
    todos.pop(index)
    storage.save_todos(todos)
    del st.session_state[id]
    st.success(f'"{title}" is complete!', icon="✅")


st.title('TODO APP')

st.text_input(
    'Enter your TODO',
    placeholder='ToDo',
    key='new_todo',
    on_change=handle_add_todo
)

for index, todo in enumerate(todos):
    id, title = todo
    st.checkbox(
        title,
        key=id,
        args=(id, title, index),
        on_change=handle_checkbox_change
    )
