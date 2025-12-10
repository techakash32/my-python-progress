class a:
    def display(self):
        print("Class A method called")
class b(a):
    def display1(self):
        print("Class B method called")
class c(b):
    def display3(self):
        print("Class C method called")

obj = c()
obj.display()
obj.display1()
obj.display3()