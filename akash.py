class a:
    def info(self):
        print("hii")
class b:
    def info(self):
        print("hello")
class c(a, b):
    pass

obj = c()
obj.info()