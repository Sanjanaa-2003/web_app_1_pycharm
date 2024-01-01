import streamlit as st
import functions

todos=functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]+"\n"    #adds list items in new lines in app
    todos.append(todo)  #appends to todos.txt file
    functions.write_todos(todos)

st.title("My To-Do App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:    #if box is checked
        todos.pop(index)    #index is popped
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


# RUN" streamlit run E:\pythonprojects\web.py " in terminal