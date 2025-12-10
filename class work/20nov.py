#requirement argument

def sum(a,b,c):
    print("output",a,b,c)

sum(1,2,3) #parameter are equal to argument not to be empty

# positional argument

def akash(x,y,z):
    print("output",x,y,z)

akash(10,20,30)
akash(30,20,10)
#based on position data pass hoga

# keyword argument

def  mul(a,b):
    print("output",a,b)
mul(a=10,b=20)
mul(b=10,a=20)

#deafault argument

def test(num="akash",num2="nagar"):
    print("output:",num,num2)

test()
test("gaurav")
test("naksh","mittal")

#variable length argument

def add(*num):
    print(num)

add()
add(1,2,4,4,8,5,4,5)
add(1,7,8,6,4,5,9,4,2,4,5,7,8,6,2,1,4,5,5,5,4,1,2)

#keyword variable length argument

def detail(**text):
    print(text)
detail()
detail(name="akash",age=48,degree="BCA")