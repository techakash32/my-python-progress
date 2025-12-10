#access modifiers:

'''



'''
class A:
    var=10
    _var1=20

class B:
    def info(self):
        print("B class",A._var1)         #public member accessed
obj=B()
obj.info()

'''


#private variable:

'''
class C:
    __var=100          #private variable

    def display(self):
        print("private variable is:",C.__var)
x=C._C__var
print("outside the class:",x)      #accessing private variable outside the class
obj1=C()
obj1.display()
#accessing private variable inside the class

