def hello():
    print("hello world")
    print("akash")
    print("gaurav")
hello()

#also take user inpUt
def userdata():
    x=56
    print(x)

userdata()

#greetings 
def greeting(user):
    print(f"hey user good morning",user)
greeting("akash")
greeting("gaurav")


course="python"
def addtwo(x,z):  # the z is called the parameter and it is used to declare at the time of function creating time:
    print(x,z,"total:",x+z) #local scope variable
    print(course)
addtwo(54,75)  #the values that we gave to function is argument:
addtwo(78,65)

total=54  #GLOBAL VARIABLE
def func(a,b):
    total=100 #LOCAL CAHNGES
    print("local scope",a,b)
    print(total)
    
func(5,51)
print(total)

