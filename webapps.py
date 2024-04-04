import streamlit as st
import functions


def add_todo(): #creating a function to be able to allow the user to add a value o the list
    todo = st.session_state["new_todo"] + "\n" #session_state is a dictionary like object to store and retrieve session-specific info
                             #also allows you to access and modify variables different parts of your streamlit app
    todos.append(todo)
    functions.write_todos(todos) #use the functions write todos to write the updated ##to#do in the to#do.txt file

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")




for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)   #write the updated tod#do with the new to#do
        del st.session_state[todo] #delete the item from the session state dictionary
        st.rerun()    #rerun the code (because it is needed for checkboxes

st.text_input(label="Enter a todo", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo') #the key identified the sg.text_input widgets
#add a lable "enter a todods" and a placeholder

