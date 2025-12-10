"""
======================================
📌 PYTHON `return` STATEMENT :
======================================

The `return` statement is used inside a function to send back a result.
It is different from `print()` because:
--------------------------------------------------
✔ `print()` only displays the value on the screen.
✔ `return` sends the value back to the program so it can be stored or used later.

Once a function executes `return`, the function STOPS immediately.
Any code after `return` will NOT run.

Syntax:
-------

def function_name():
    return value

"""

# 1️⃣ BASIC EXAMPLE OF RETURN
# ---------------------------
# Function performs an operation and returns the result.

def shadi(num):
    print("Lifafa is of:", num + 1000)
    return num + 1000  # returning result

# Storing returned value
x = shadi(5000)
print("Returned value:", x)


# 2️⃣ USING RETURN VALUE IN PROGRAM
# ---------------------------------
# Returned value can be used for further calculations.

def multiply(a, b):
    return a * b

result = multiply(10, 5)
print("Multiplication Result:", result)
print("Result × 2:", result * 2)


# 3️⃣ RETURN MULTIPLE VALUES
# --------------------------
# You can return more than one value (stored as a TUPLE).

def student():
    name = "Akash"
    age = 22
    return name, age

info = student()
print("Student Info:", info)  # tuple output


# 4️⃣ RETURN VS PRINT DIFFERENCE
# -------------------------------

def example():
    return 10

print(example())  # prints value returned by function

# Using print inside function:

def example2():
    print(10)

example2()  # prints 10 but returns None (nothing)


# 5️⃣ RETURN EXITS FUNCTION IMMEDIATELY
# --------------------------------------

def check():
    print("Before return")
    return "Function Ended"
    print("This will NOT run")

print(check())


"""
SUMMARY
-------
✔ `return` sends a value back from a function.
✔ After `return`, the function stops executing.
✔ Returned values can be stored, reused, or processed.
✔ Can return single or multiple values.
✔ `print()` shows output, `return` gives usable value.

End of Notes.
"""