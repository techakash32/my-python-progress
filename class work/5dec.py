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

