'''
Docstring for PYTHON.OOPS CONCEPT.OOPS
====================================================================
📌 OBJECT-ORIENTED PROGRAMMING (OOPS) — NOTES + EXAMPLES
====================================================================

DEFINITION:
-----------
OOPS (Object-Oriented Programming System) is a programming model
based on the concept of classes and objects. It organizes code into
modular, reusable, and logical components.
  
WHY DO WE USE OOPS?
-------------------
✔ To make code modular (divided into classes)  
✔ To reuse code using inheritance  
✔ To secure data using encapsulation  
✔ To perform one action in multiple ways (polymorphism)  
✔ To hide unnecessary details (abstraction)  
✔ To make large programs easier to maintain  
✔ To structure real-world problems into objects  

CORE FEATURES OF OOPS:
-----------------------
1️⃣ Class & Object  
2️⃣ Inheritance  
3️⃣ Polymorphism  
4️⃣ Encapsulation  
5️⃣ Abstraction  

====================================================================
# 1️⃣ CLASS & OBJECT
# ---------------------------------------------------------------
DEFINITION:
A class is a blueprint/template.  
An object is an instance created from that class.

USE:
✔ Represent real-world entities  
✔ Group related data + functions together  
====================================================================
"""

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print("Name:", self.name, "| Roll:", self.roll)

s1 = Student("Akash", 101)
s1.show()

print("------------------------------------------------------------")
"""
====================================================================
# 2️⃣ INHERITANCE
# ---------------------------------------------------------------
DEFINITION:
Inheritance allows one class (child) to acquire the properties and
methods of another class (parent).

USE:
✔ Code reusability  
✔ Better organization  
✔ Extending existing functionalities  
====================================================================
"""

class Parent:
    def home(self):
        print("Parent has a house")

class Child(Parent):
    def car(self):
        print("Child has a car")

c = Child()
c.home()
c.car()

print("------------------------------------------------------------")
"""
====================================================================
# 3️⃣ POLYMORPHISM
# ---------------------------------------------------------------
DEFINITION:
Polymorphism means "one task, many forms."  
The same function name behaves differently depending on context.

TYPES:
✔ Method Overriding  
✔ Duck Typing  
✔ Operator Overloading  
====================================================================
"""

class Bird:
    def sound(self):
        print("Bird makes sound")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

b = Sparrow()
b.sound()

print("------------------------------------------------------------")
"""
====================================================================
# 4️⃣ ENCAPSULATION
# ---------------------------------------------------------------
DEFINITION:
Encapsulation means combining data + methods inside a class and
restricting direct access using access modifiers.

USE:
✔ Protect sensitive data  
✔ Avoid accidental modification  
✔ Maintain code security  
====================================================================
"""

class Bank:
    def __init__(self):
        self.__balance = 5000   # private

    def show_balance(self):
        print("Balance =", self.__balance)

b = Bank()
b.show_balance()

print("------------------------------------------------------------")
"""
====================================================================
# 5️⃣ ABSTRACTION
# ---------------------------------------------------------------
DEFINITION:
Abstraction means hiding complex details and showing only what is
necessary.

USE:
✔ Reduce complexity  
✔ Hide internal logic  
✔ Provide clean & simple interfaces  
====================================================================
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

c = Car()
c.start()

print("------------------------------------------------------------")
"""
====================================================================
SUMMARY OF OOPS
====================================================================

✔ CLASS & OBJECT  
   → Blueprint & instance  
   → Helps structure data + behavior  

✔ INHERITANCE  
   → Reuse code  
   → Parent-child relationship  

✔ POLYMORPHISM  
   → One action, many forms  

✔ ENCAPSULATION  
   → Protects data  
   → Uses access modifiers  

✔ ABSTRACTION  
   → Hides complex details  
   → Clean interface for users  

✔ OOPS helps in:
   • Code reusability  
   • Data security  
   • Modular program design  
   • Large-scale project handling  

END OF NOTES.
'''