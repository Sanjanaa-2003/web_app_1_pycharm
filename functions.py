def get_todos(filepath='todos.txt'):        #function to read todos
    """Read a text file and return the list of todo items
    """
    with open(filepath, 'r') as file:  # by default read mode
        todos = file.readlines()
    return todos
def write_todos(todos_arg,filepath='todos.txt'):    #this has tp be order of arguments else raises error        #function to read todos
    """Write the todo items list in the text file"""
    with open(filepath, 'w') as file:  # by default read mode
       file.writelines(todos_arg)
    # return todos_arg
print("Hello from functions")
print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())

