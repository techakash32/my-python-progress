#PYTHON INHERITANCE : 
class RegexEduhub:
    profit="10 crores"

#parent chid class
class Regexsoftware(RegexEduhub):
    student=1000

print("*******************************")

# creating object of child class

class Tatamotors:
    employee=5000
    revenue="500 crores"

    def info(self):
        print("This is Tata motors class","employee =",self.employee,"profit =",self.revenue)

class tataharier(Tatamotors):
    model="harrier"
    price="20 lakhs"
    def infoharier(self):
        print("This is Tata Harrier class")
        super().info()


t1=tataharier()
t1.infoharier()

print("*******************************")
class customer:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
    def get_info(self):
        print("getting info",self.name,self.email,self.phone)
class driver(customer):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
d1=driver("John","john@example.com","1234567890")
print(d1.name,d1.email,d1.phone)