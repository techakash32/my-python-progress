#constructur

'''
functions/methods  which are used to initialize the object
when an object is created
it is called automatically
__init__() is a special method
'''
class housedesign:
    color='white'
    price=500000
class housedesign:
    def __init__(self):  #constructor
        print("this is constructor,builder ko bulaya ja rha h")

h1=housedesign()  #object created and constructor called automatically
print(h1)

#self=it is a reference variable which refers to the current object of the class

class housedesign:
    def __init__(self,color,price):  #parameterized constructor
        self.color=color #instance variable 
        self.price=price #instance variable 
h1=housedesign("red",600000)
print(h1.color)
print(h1.price)

print("*******************************")



