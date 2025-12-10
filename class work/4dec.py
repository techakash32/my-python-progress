#class variable acessing and modifying 

print("*******************************")

class valuecounts:
    x=0
    def __init__(self):
        self.x=self.x+1

#if changing class varible it show to every object also for that class
#but if changing object varible it will change only for that object not for class and other objects.

v1=valuecounts()
print(v1.x)

v2=valuecounts()
print(v2.x)


print("*******************************")

class valuecounts:
    x=0
    def __init__(self):
        valuecounts.x=valuecounts.x+1   #class varible changing using class name
#object varible changing using class varible

v3=valuecounts()
print(v3.x)

v4=valuecounts()
print(v4.x)

v5=valuecounts()
print(v5.x)

print("*******************************")