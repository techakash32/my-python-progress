"""
======================================
📌 PYTHON FUNCTION ARGUMENT TYPES (NOTES + EXAMPLES)
======================================

This file explains different types of function arguments in Python with examples.
Arguments define how values are passed to functions.

Types of Arguments:
-------------------
1️⃣ Required Argument
2️⃣ Positional Argument
3️⃣ Keyword Argument
4️⃣ Default Argument
5️⃣ Variable-Length Argument (*args)
6️⃣ Keyword Variable-Length Argument (**kwargs)

"""

# 1️⃣ REQUIRED ARGUMENT
# ----------------------
# Number of arguments must match number of parameters.
# If missing, Python throws an error.

def sum(a, b, c):
    print("Output:", a, b, c)

sum(1, 2, 3)  # Correct
# sum(1, 2)  ❌ Missing argument will give error

# ----------------------------------------------------

# 2️⃣ POSITIONAL ARGUMENT
# -----------------------
# Values are assigned based on POSITION.

def akash(x, y, z):
    print("Output:", x, y, z)

akash(10, 20, 30)
akash(30, 20, 10)  # Order affects meaning

# ----------------------------------------------------

# 3️⃣ KEYWORD ARGUMENT
# --------------------
# Parameter names are used during call.
# Order does NOT matter.

def mul(a, b):
    print("Output:", a, b)

mul(a=10, b=20)
mul(b=10, a=20)  # Order swapped

# ----------------------------------------------------

# 4️⃣ DEFAULT ARGUMENT
# --------------------
# If no value is passed, default value is used.

def test(num="Akash", num2="Nagar"):
    print("Output:", num, num2)

# Uses default values
test()
# Overrides first value
test("Gaurav")
# Overrides both values
test("Naksh", "Mittal")

# ----------------------------------------------------

# 5️⃣ VARIABLE LENGTH ARGUMENT (*args)
# -----------------------------------
# Can accept multiple parameters.
# Values are stored in a TUPLE.

def add(*num):
    print(num)

add()
add(1, 2, 4, 4, 8, 5, 4, 5)
add(1, 7, 8, 6, 4, 5, 9, 4, 2, 4, 5, 7, 8, 6, 2, 1, 4, 5, 5, 5, 4, 1, 2)

# ----------------------------------------------------

# 6️⃣ KEYWORD VARIABLE LENGTH ARGUMENT (**kwargs)
# ------------------------------------------------
# Accepts multiple keyword arguments.
# Stored in a DICTIONARY.

def detail(**text):
    print(text)

# No arguments
detail()
# With arguments
detail(name="Akash", age=48, degree="BCA")


"""
SUMMARY TABLE
-------------
| Type | Example | Order Matters? | Stores As |
|------|---------|----------------|-----------|
| Required | sum(a,b,c) | Yes | Single Values |
| Positional | func(10,20) | Yes | Single Values |
| Keyword | func(a=10,b=20) | No | Single Values |
| Default | func(a=10) | Optional | Single Values |
| *args | func(1,2,3) | No | Tuple |
| **kwargs | func(a=10,b=20) | No | Dictionary |

✔ Best practice: Function structure order should be → positional → default → *args → **kwargs

End of Notes.
"""