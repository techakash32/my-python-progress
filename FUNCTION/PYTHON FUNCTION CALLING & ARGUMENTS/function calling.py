# ============================================================
#   PYTHON FUNCTION CALLING & ARGUMENTS (NOTES)
# ============================================================

# Python uses "Call by Object Reference" (Call by Sharing).
# Meaning: The function gets a reference to the object, NOT a copy.
# Behavior depends on whether the object is MUTABLE or IMMUTABLE.

# Mutable Objects → list, dict, set, bytearray (Changes reflect)
# Immutable Objects → int, float, bool, tuple, str, frozenset (Changes DO NOT reflect)



# ------------------------------------------------------------
# 1️⃣ Call by Value-like behavior (IMMUTABLE OBJECTS)
# ------------------------------------------------------------

def immut_func(z):
    # Print object memory before change
    print("Memory before change:", id(z))
    
    # Assigning new value creates a NEW memory location
    z = 20
    print("Memory after change:", id(z))

a = 10
immut_func(a)
print("Original variable memory:", id(a))   # remains unchanged


# ------------------------------------------------------------
# 2️⃣ Call by Reference-like behavior (MUTABLE OBJECTS)
# ------------------------------------------------------------

def mut_func(z):
    print("Memory before append:", id(z))
    
    # Modifies original list because LIST is mutable
    z.append(45)
    
    print("Updated list:", z)
    print("Memory after append:", id(z))

mylist = [10, 20]
mut_func(mylist)
print("Original list memory:", id(mylist))  # remains same


# ------------------------------------------------------------
# 3️⃣ Local vs Global Scope Example
# ------------------------------------------------------------

num = 10  # Global variable

def show_scope():
    num = 20  # Local variable (temporary inside function)
    print("Inside function:", num)

show_scope()
print("Outside function:", num)  # Global value unchanged


# ------------------------------------------------------------
# 4️⃣ Using 'global' keyword to modify global variable
# ------------------------------------------------------------

num2 = 10

def modify_global():
    global num2  # Allows modification of global scope variable
    num2 = 20
    print("Inside function:", num2)

modify_global()
print("Outside function:", num2)  # Updated


# ------------------------------------------------------------
# 5️⃣ *args → Variable length positional arguments
# ------------------------------------------------------------

def show_args(*nums):
    # *args collects multiple values as a TUPLE
    print("Args received:", nums)

show_args(10, 20, 30)


# ------------------------------------------------------------
# 6️⃣ **kwargs → Variable length keyword arguments
# ------------------------------------------------------------

def show_kwargs(**details):
    # **kwargs collects key:value pairs as a DICTIONARY
    print("Keyword args received:", details)

show_kwargs(name="Akash", age=48, degree="BCA")


# ------------------------------------------------------------
# 7️⃣ COMMON ERROR: Mutable default argument ⚠️
# ------------------------------------------------------------

def wrong_default(a, b=[]):
    # This list persists across multiple calls → risky!
    b.append(a)
    print("Value:", a, "| List:", b)

wrong_default(10)
wrong_default(20)
wrong_default(60)
wrong_default(50, [])  # Fix: new list provided


# ------------------------------------------------------------
# 8️⃣ Correct Fix (SAFE method)
# ------------------------------------------------------------

def correct_default(a, b=None):
    if b is None:
        b = []  # Create new list each time
    b.append(a)
    print("Value:", a, "| List:", b)

correct_default(10)
correct_default(20)
correct_default(30)


# ------------------------------------------------------------
# 9️⃣ Quick Table Summary (Just for learning, not code)
# ------------------------------------------------------------

# Required Argument            → func(a, b)
# Positional Argument          → func(10, 20)
# Keyword Argument             → func(a=10, b=20)
# Default Argument             → func(a=10)
# *args (variable positional)  → func(1, 2, 3)
# **kwargs (variable keyword)  → func(name="Akash", age=20)
# Passing function as argument → map(len, ["hi", "ok"])



# ------------------------------------------------------------
# 🧠 INTERVIEW MCQ (Answers in comments)
# ------------------------------------------------------------

# 1) Python uses which model?
# → Call by Object Reference ✔

# 2) Data type of *args?
# → Tuple ✔

# 3) What happens with mutable default argument?
# → Shared list across calls ✔

# 4) Which keyword modifies global variable?
# → global ✔

# 5) What does **kwargs store data as?
# → Dictionary ✔


# ------------------------------------------------------------
# 🎯 SUMMARY
# ------------------------------------------------------------
# ✔ Python uses Call by Object Reference
# ✔ Mutable objects change outside function
# ✔ Immutable objects do NOT change
# ✔ Use *args for multiple values
# ✔ Use **kwargs for multiple named values
# ✔ Avoid b=[] in arguments → use b=None instead
# ✔ Use global when updating global variable inside function

