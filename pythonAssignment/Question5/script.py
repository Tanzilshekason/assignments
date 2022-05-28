import os

# Create a new folder using script
def my_function():
    path = "/home/neosoft/Documents/Assignments/PythonAssignment/Question5"
    os.chdir(path)
    Newfolder = 'Read me'
    os.makedirs(Newfolder)

    my_function()
