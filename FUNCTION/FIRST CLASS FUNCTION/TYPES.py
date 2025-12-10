"""
======================================
📌 FIRST-CLASS FUNCTIONS IN PYTHON (NOTES + EXAMPLES)
======================================

Python treats functions as **first-class citizens**, meaning:
✔ Functions can be stored in variables
✔ Passed as arguments to other functions
✔ Returned from functions
✔ Stored in data structures (list, dict, tuple)

This concept allows Python to support **higher-order functions**, functional programming patterns, and callbacks.

"""


# 1️⃣ ASSIGN FUNCTION TO A VARIABLE
# --------------------------------
# A function can be stored in a variable and called from it.

def func():
    print("Hi!")

# Assign function to variable `a`
a = func
print(a, func)  # Both point to same function

# Call using variable
a()


# 2️⃣ STORE FUNCTION INSIDE DATA STRUCTURES
# -----------------------------------------
# Functions can be stored in list, tuple, dictionary, etc.

mylist = [10, 20, func]
mylist[-1]()  # Calling function stored in list


# 3️⃣ PASS FUNCTION AS ARGUMENT
# -----------------------------
# One function can receive another function as input.

def addnumber(num):
    return num + 1

def twonumber(x, y):  # y is a function
    print("Value of x:", x)
    print("Calling function y:", y())

twonumber(6, addnumber)  # Passing function addnumber


# 4️⃣ FUNCTION RETURN ANOTHER FUNCTION (Nested Return)
# ----------------------------------------------------

def greet(name):
    def message():
        return f"Hello, {name}!"
    return message  # Returning function, NOT calling it

returned_func = greet("Akash")
print(returned_func())  # Calling inner function


# 5️⃣ HIGHER ORDER FUNCTION
# -------------------------
# A function that takes another function OR returns another function.

# Example: Applying a function to numbers using higher-order function

def operate(fn, value):
    return fn(value)

print(operate(addnumber, 10))


"""
SUMMARY
-------
Python treats functions like normal values, so they can:
✔ Be assigned to a variable
✔ Be passed as an argument
✔ Be returned from another function
✔ Be stored in a data structure

This makes Python powerful for:
➡ Callback functions
➡ Decorators
➡ Functional programming
➡ Event handling
➡ Machine learning pipelines

End of Notes.
"""