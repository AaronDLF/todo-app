import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
  todo = st.session_state["new_todo"] + "\n"
  todos.append(todo)
  functions.write_todos(todos)


st.title("To-Do App")
st.subheader("Manage your tasks easily")

for todo in todos:
  st.checkbox(todo)


st.text_input(label="", placeholder="Add a new to-do...", on_change=add_todo, key="new_todo")


