#python follow call by object refrence: 

# mutable--> list,dict,set
#immutable --> int,float,frozenset,bool,str
#call by value

def func(z):
    print(id(z))
    z=20            #immutable
    print(id(z))   #change the address of z beascue we assign it 20
a=10
func(a)
print(id(a))

#3 output
#mutable ,call by adress/refrence

def func(z):
    print(id(z))
    z.append(45)
    print(z)
    print(id(z))

a=[10,20]
func(a)
print(id(a))

#mutable --> call by refrence/adress
#immutable -->call by value

#example

num=10
def test():
    num=20
    print(num)
test()
print(num)

# after global

num=10
def test():
    global num
    num=20
    print(num)
test()
print(num)

#impotant

def test(*y,**x):
    print(y,x)
x=test(41,3,23,2,hii=100)  #same order warna error
print(x)

#function overright
def func(a,b=[]):
    b.append(a)
    print(a,b)

func(10)
func(20)
func(60)
func(50,[])

# 


