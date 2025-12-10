"""
====================================================================
📌 PYTHON ACCESS MODIFIERS (NOTES + EXAMPLES)
====================================================================

Access Modifiers are used to control the visibility of variables
and methods inside a class and outside the class.

# - WHY DO WE USE ACCESS MODIFIERS - ?
-------------------------------
✔ To protect sensitive data
✔ To prevent accidental modification  
✔ To implement Encapsulation  
✔ To organize code & maintain security  
✔ To give controlled access using methods  

TYPES OF ACCESS MODIFIERS IN PYTHON:
------------------------------------
1️⃣ Public         → full access everywhere  
2️⃣ Protected      → limited access (class + subclass)  
3️⃣ Private        → restricted access (inside class only)
 4. deafult       -> its a deafult access modifier(same package)

NOTE:
Python does NOT enforce strict access control.
It follows naming conventions instead.

===================================================================
# 1️⃣ PUBLIC MEMBERS (Default)
# ---------------------------------------------------------------
DEFINITION:
Public members can be accessed anywhere (inside class, outside class,
subclasses, objects). No underscore is used.

USE:
✔ Use when the data/method should be openly accessible.
===================================================================
"""

class PublicDemo:
    def __init__(self):
        self.name = "Akash"   # public variable

    def display(self):        # public method
        print("Name =", self.name)

obj = PublicDemo()
obj.display()
print(obj.name)   # public → accessible everywhere


print("------------------------------------------------------------")
"""
====================================================================
# 2️⃣ PROTECTED MEMBERS (_variable)
# ---------------------------------------------------------------
DEFINITION:
Protected members start with ONE underscore (_) and are accessible
inside the class and in subclasses.

#protected members = they are accessible within the same package and also available to all subclasses.
also have inheritance.

USE:
✔ When you want to allow partial access
✔ Prevent accidental use outside class
====================================================================
"""

class ProtectedDemo:
    def __init__(self):
        self._balance = 5000   # protected variable

    def _show_balance(self):   # protected method
        print("Balance =", self._balance)

class Bank(ProtectedDemo):
    def access_balance(self):
        print("Accessing protected member inside subclass:")
        self._show_balance()

b = Bank()
b.access_balance()

# Technically accessible but not recommended
print(b._balance)


print("------------------------------------------------------------")
"""
====================================================================
# 3️⃣ PRIVATE MEMBERS (__variable)
# ---------------------------------------------------------------
DEFINITION:
Private members start with TWO underscores (__) and can only be
accessed inside the class. Python applies *name mangling* internally:
__var → _ClassName__var

USE:
✔ Hide sensitive data completely  
✔ Allow access only using getter/setter methods  
✔ Prevent accidental modification  
====================================================================
"""

class PrivateDemo:
    def __init__(self):
        self.__pin = 1234       # private variable

    def __show_pin(self):       # private method
        print("PIN =", self.__pin)

    def access_private(self):
        print("Accessing private inside class:")
        self.__show_pin()

p = PrivateDemo()
p.access_private()

# ❌ Direct access = ERROR
# print(p.__pin)

# ✔ Access using name-mangling (not recommended)
print(p._PrivateDemo__pin)


print("------------------------------------------------------------")
"""
====================================================================
SUMMARY
====================================================================
✔ PUBLIC (name)  
    → Accessible everywhere  
    → Use for general data & functions

✔ PROTECTED (_name)  
    → Accessible in class + child class  
    → Use for semi-secure data

✔ PRIVATE (__name)  
    → Accessible ONLY inside class  
    → Use for highly sensitive data  
    → Uses name-mangling → _ClassName__var

✔ Access Modifiers help in:
    • Encapsulation  
    • Security  
    • Code organization  
    • Preventing accidental misuse  

END OF NOTES.
"""
