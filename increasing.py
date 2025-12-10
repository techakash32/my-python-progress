class a:
    def __init__(self):
        print("class a")
        super().__init__()

class b(a):
    def __init__(self):
        print("class b")
        super().__init__()
class c(b):
    def __init__(self):
        print("class c")
        super().__init__()

obj = c()
print("*******************************")
obj2 = b()
print("*******************************")
obj3 = a()
print("*******************************")