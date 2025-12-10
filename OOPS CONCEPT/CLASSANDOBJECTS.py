"""
======================================
📌 PYTHON OOP — CLASS & OBJECT NOTES (WITH EXAMPLES)
======================================

A class is a blueprint for creating objects.
it is a template where we can store collection of object like variable,function.
a class is LOGICAL ENTITY. 

Objects = Instance of a class
object = it is a realworld entity.
it is a real world entity.

Class variables = Shared by all objects  
Instance variables = Unique for each object

SUMMARY:
--------
✔ Class variable = shared by all objects  
✔ Instance variable = only for that object  
✔ Assigning using object creates instance variable  
✔ Assigning using class changes class variable for EVERY object

FINAL NOTES
-----------
✔ Classes create structure.
✔ Objects store data.
✔ Class variables → common for all.
✔ Instance variables → specific to each object.
✔ Methods use `self` to access REALTIME object/class data.

"""


# 1️⃣ BASIC CLASS WITH CLASS VARIABLES
# ------------------------------------

class housedesign:
    color = 'white'
    price = 500000

# Create object
tushar_home = housedesign()   # object = class()

print(tushar_home, tushar_home.color)
print(tushar_home, tushar_home.price)


# 2️⃣ MULTIPLE OBJECTS OF SAME CLASS
# ----------------------------------

t2 = housedesign()
print(t2.color)        # white (default)

t2.color = 'red'       # changing only this instance variable
print(t2.color)        # red
print(tushar_home.color)  # still white → class variable remains same


"""
👉 NOTE:
Changing class variable using *object* creates an INSTANCE VARIABLE,
so it affects only that specific object.
"""


# 3️⃣ ACCESSING CLASS VARIABLES INSIDE METHODS
# -------------------------------------------

class housedesign:
    color = 'white'
    price = 500000
    
    def info(self):
        print(self.color, self.price)


h3 = housedesign()
h3.info()              # white 500000
print(h3.color)


"""
📌 IMPORTANT:
self.variable → accesses the class variable OR instance variable  
"""


# 4️⃣ CLASS VARIABLE VS INSTANCE VARIABLE
# ---------------------------------------

h4 = housedesign()
h4.color = 'blue'      # instance variable created
print(h4.color)        # blue
print(h3.color)        # white → unaffected


"""

"""


# 5️⃣ ANOTHER CLASS EXAMPLE
# -------------------------

class employeesignup:
    company = 'regex'
    c_mail = 'regex@gmail.com'
    turnover = "100 crore"
    
    def info(self):
        print(self.c_mail, self.c_mail.split('@')[1])
        # self.c_mail → regex@gmail.com
        # split('@')[1] → "gmail.com"


e1 = employeesignup()
e1.info()


"""


ENd of Notes.
"""
