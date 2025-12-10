# first class function

# 1. assign to a variable

def func():
    print("hii")
a=func
print(a,func)
a()

# 2. function can be strored as data structure

mylist=[10,20,func]
mylist[-1]()

#3. pass a function as a argument


def addnumber(num):
    return num+1
def twonumber(x,y):
    print(x,y)
    print(y())
twonumber(6,addnumber)



