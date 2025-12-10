"""FUNCTIONS IN PYTHON
=============================
A **function** is a reusable block of code that performs a specific task.
Functions help write clean, organized, and reusable code.

Syntax:
--------

def function_name(parameters):
    # function body
    statements

You can call the function by using its name followed by parentheses:
function_name()

"""

# ==============================
# Example 1: Simple Function
# ==============================
# This function prints three lines of text.
# "def" is the keyword used to define a function.
# The function name here is "hello".
# Inside the function, print statements are executed only when function is called.

def hello():
    print("Hello world")
    print("Akash")
    print("Gaurav")

# Calling the function
hello()  # Without calling, function will NOT run.


# ==============================
# Example 2: Function With Local Variables
# ==============================
# Variables declared inside a function are called LOCAL VARIABLES.
# They exist only inside the function and cannot be used outside.


def userdata():
    x = 56  # Local variable
    print(x)

userdata()  # Calling function


# ==============================
# Example 3: Function With Parameters and Arguments
# ==============================
# "user" here is a parameter → used during function definition.
# When calling function and passing value (e.g., "Akash"), that value is called an ARGUMENT.

def greeting(user):  # user -> parameter
    print(f"Hey {user}, good morning!")

# Passing argument values while calling

greeting("Akash")
greeting("Gaurav")


# ==============================
# Example 4: Using Parameters to Perform Calculations
# ==============================
# "x" and "z" are parameters.
# Values passed to them are arguments.
# "course" is GLOBAL variable so it can be accessed inside and outside functions.

course = "Python"

def addtwo(x, z):  # Parameter definition
    print(x, z, "Total:", x + z)  # Performing addition
    print(course)  # Accessing global variable

addtwo(54, 75)  # Argument values
addtwo(78, 65)


# ==============================
# Example 5: Global vs Local Variable
# ==============================
# If variable is created outside function → GLOBAL SCOPE
# If created inside → LOCAL SCOPE
# Local scope has priority when inside function


total = 54  # Global variable

def func(a, b):
    total = 100  # Local variable (shadowing global)
    print("Local scope values:", a, b)
    print("Local total:", total)  # This prints local version

func(5, 51)
print("Global total:", total)  # This prints global version


# ==============================
# Example 6: Taking User Input Inside Function
# ==============================

def take_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}, your age is {age}.")

# Uncomment below line to test (input only works when running Python file)
# take_input()


"""
SUMMARY:
--------
✔ Functions help reuse code.
✔ `def` is used to define a function.
✔ Parameters are placeholders declared in function.
✔ Arguments are actual values passed to function.
✔ Local variables exist only inside function.
✔ Global variables can be accessed anywhere.
✔ Input can be taken inside a function.

End of Notes.
"""
