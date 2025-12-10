"""
======================================
📌 PYTHON CONSTRUCTOR (__init__) NOTES + EXAMPLES
======================================

A constructor is a special method used to **initialize an object**.

✔ __init__ runs automatically when object is created  
✔ Used to initialize object data  
✔ self refers to the object's memory  
✔ You can create parameterized constructors to store values  
✔ Instance variables are created inside __init__ using self

✔ Runs automatically when an object is created  
✔ Method name is always:  __init__()  
✔ Used to assign values to instance variables

__init__() →  constructor


"""


# 1️⃣ DEFAULT CONSTRUCTOR (No parameters)
# ---------------------------------------

class housedesign:
    color = 'white'
    price = 500000


class housedesign:
    def __init__(self):   # Constructor
        print("This is constructor, builder ko bulaya ja rha h")


h1 = housedesign()   # Object created → constructor runs automatically
print(h1)


"""
📌 self  
`self` is a reference variable that points to the CURRENT object.
Used to access instance variables.
"""


# 2️⃣ PARAMETERIZED CONSTRUCTOR
# -----------------------------

class housedesign:
    def __init__(self, color, price):   # parameterized constructor
        self.color = color     # instance variable
        self.price = price     # instance variable

print("*******************************")

h1 = housedesign("red", 600000)
print(h1.color)       # red
print(h1.price)       # 600000

print("*******************************")

h2 = housedesign("white", 1000000)
print(h2.color)       # white
print(h2.price)       # 1000000

print("*******************************")


"""
SUMMARY
-------


End of Notes.
"""
