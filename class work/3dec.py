class housedesign:
    color='white'
    price=500000
tushar_home=housedesign()
#object=class()
print(tushar_home,tushar_home.color)
print(tushar_home,tushar_home.price)

t2=housedesign()
print(t2.color)
t2.color='red'
print(t2.color) #CLASS VARIBALE CHANGED ONLY FOR INSTANCE VARIABLE NOT FOR ALL
print(tushar_home.color) #FOR THIS CLASS VARIABLE REMAINS SAME

class housedesign:
    color='white'
    price=500000
    def info(self):
        print(self.color,self.price) #for the function to access class variable we use self.
h3=housedesign()
h3.info()
print(h3.color)

#class variable are the varible can be used with the class and also for objects

#object varible change only for that object not the class
#class varible change class and also every its object

h4=housedesign()
h4.color='blue'
print(h4.color)
print(h3.color)

class employeesignup(self):
    company='regex'
    c_mail='regex@gmail.com'
    turnover="100 crore"
    
    def info(self):
        print(self.c_mail,self.c_mail.split('@')[1]) #to get the name before @ in email

e1=employeesignup()
e1.info()

