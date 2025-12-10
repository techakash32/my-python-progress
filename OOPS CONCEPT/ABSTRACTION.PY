"""
===============================================================
📌 PYTHON ABSTRACTION (NOTES + EXAMPLES)
===============================================================

Abstraction → Hiding internal implementation and showing only
the essential features to the user.

It is achieved using:
✔  Abstract Classes  
✔ Abstract Methods  
✔ 'abc' module (Abstract Base Class)

---------------------------------------------------------------
Why Abstraction :
---------------------------------------------------------------
✔ Hides complex code  
✔ Shows only necessary things  
✔ Improves security  
✔ Reduces code complexity  
✔ Helps in building large applications

===============================================================
# 1️⃣ ABSTRACT CLASS & ABSTRACT METHOD
# (We use abc.ABC and @abstractmethod)
===============================================================

An abstract class := it is a blueprint for other classes.
It is used when you want to define a common structure for all child classes 
but you don't want the parent class to be directly created (no object of it).

An abstract method is an empty method in the parent class 
that must be completed in child classes.

##  Why do we use an abstract class?  ##

To force child classes to implement certain methods
(like a rule: “Every child must have this method”).

To create a common structure for related classes.

To prevent creating objects from the parent class — because it's incomplete.

To achieve partial abstraction (some methods can have body, some not).
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):              # Abstract class
    @abstractmethod
    def start(self):             # Abstract method
        pass

    def info(self):              # Normal method
        print("This is a vehicle.")

class Car(Vehicle):              # Child class must implement start()
    def start(self):
        print("Car starts with a key.")

c = Car()
c.start()
c.info()

a=Vehicle  # Abstract class cannot be instantiated
# a.start()  ❌ ERROR

print("---------------------------------------------------------")
"""
===============================================================
# 2️⃣ ANOTHER EXAMPLE – BANK SYSTEM
===============================================================
"""

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class SBI(Bank):
    def deposit(self):
        print("Depositing money in SBI...")

    def withdraw(self):
        print("Withdrawing money from SBI...")

b = SBI()
b.deposit()
b.withdraw()


print("---------------------------------------------------------")
"""
===============================================================
# 3️⃣ ABSTRACT CLASS CANNOT BE INSTANTIATED
===============================================================

obj = Vehicle()   ❌ ERROR
You must create a child class and implement all abstract methods.
"""


"""
===============================================================
SUMMARY
---------------------------------------------------------------
✔ Abstraction hides internal details  
✔ abc.ABC is used to create abstract classes  
✔ @abstractmethod forces child classes to implement methods  
✔ Abstract class cannot be directly instantiated  
✔ Supports secure, clean, modular programming

END OF NOTES.
"""
