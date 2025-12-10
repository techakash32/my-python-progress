#constructor chaining in inheritance
class A:
    def __init__(self):
        print("Constructor of class A called")
class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of class B called")
a1=B()

print("-------------------")

#polymorphism :it is a unique feature of oops ans used to perform a single action in different ways.
'''
Polymorphism → “One thing, many forms”

It allows the same function/method/operator to behave differently
based on the object or data type.
'''

#method overloading
#method overriding

#method overloading=a class contain same name function with different parameters in a single class.

class math:
    def add(self):
        print("Addition:")
    def add(self,a):
        print("Addition: and heloo")
obj=math()
obj.add(5)

print("-------------------")
#method overriding=when a derived class contain same name function as in its base class.
#python does not support method overloading directly.

#reason1 = because python support dynamic typing.
#reason2=we use variable length argument so that we can pass any number of arguments in a function.

class X:
    def show(self):
        print("Class X method called")
    def show(self):
        print("Class X method with parameter called")
obj1=X()
obj1.show()

#name space=it is a uniqueness for each and every variable in python.

x=7
x=9  # overwriting the value of x
print(x)

print("-------------------")

#overriding: where a parent and child class contain same name method but the working is different.
#its also important to realtion between parent and child class.

class distributor:
    def shopping(self):
        print("30% discount on shopping")
class shopkeeper(distributor):
    def shopping(self):
        print("5% discount on shopping")
obj2=shopkeeper()
obj2.shopping()

print("-------------------")

#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#EXTRA#

"""
====================================================================
📌 PYTHON POLYMORPHISM (NOTES + EXAMPLES)
====================================================================


Types of Polymorphism in Python:
--------------------------------
1️⃣ Method Overriding (supported)  
2️⃣ Method Overloading (not directly supported)  
3️⃣ Operator Overloading  
4️⃣ Polymorphism with Functions & Classes

====================================================================
# 1️⃣ METHOD OVERRIDING (RUNTIME POLYMORPHISM)
# Child class changes parent class method behavior
====================================================================
"""

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()


print("------------------------------------------------------------")
"""
====================================================================
# 2️⃣ METHOD OVERLOADING (NOT SUPPORTED DIRECTLY IN PYTHON)
# Python overwrites the last defined method.
====================================================================
"""

class Math:
    def add(self, a=0, b=0, c=0):   # using default parameters
        print("Sum =", a + b + c)

m = Math()
m.add(5)
m.add(5, 10)
m.add(5, 10, 15)


print("------------------------------------------------------------")
"""
====================================================================
# 3️⃣ OPERATOR OVERLOADING
# Same operator behaves differently for user-defined objects.
====================================================================
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):      # overloading +
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)


print("------------------------------------------------------------")
"""
====================================================================
# 4️⃣ POLYMORPHISM WITH FUNCTIONS AND CLASSES
====================================================================
"""

class Car:
    def start(self):
        print("Car starts with a key")

class Bike:
    def start(self):
        print("Bike starts with a kick")

def vehicle_start(obj):     # same function → different behavior
    obj.start()

vehicle_start(Car())
vehicle_start(Bike())


print("------------------------------------------------------------")
"""
====================================================================
SUMMARY
====================================================================
✔ Polymorphism = many forms of same method / operator  
✔ Method Overriding → Child class modifies parent method  
✔ Method Overloading → Not direct; use default arguments  
✔ Operator Overloading → Using dunder methods (__add__, __str__)  
✔ Polymorphism with functions → Same function, different objects  

END OF NOTES.
"""
print("---------------------------------------------------------")