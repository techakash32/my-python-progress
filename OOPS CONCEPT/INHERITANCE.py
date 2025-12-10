"""
======================================
📌 PYTHON INHERITANCE (NOTES + EXAMPLES)
======================================

Inheritance allows one class acquire properties & methods
from another class .



#super() function is used to give access to the parent class methods and properties.
# It is used to call the parent class constructor from the child class.

SUMMARY
-------
✔ Single Inheritance     → One parent → one child  
✔ Multilevel Inheritance → Chain of classes  
✔ Multiple Inheritance   → Child inherits from multiple parents  
✔ Hybrid Inheritance     → Mix of multiple & multilevel  
✔ super() used to call parent constructor/method  
✔ DRY principle: avoids rewriting code

TYPES OF INHERITANCE:
---------------------
1️⃣ Single Inheritance  
2️⃣ Multilevel Inheritance  
3️⃣ Multiple Inheritance  
4️⃣ Hybrid Inheritance (mix of all)

"""
# ================================================================
# 1️⃣ SINGLE INHERITANCE
# ---------------------------------------------------------------

class RegexEduhub:
    profit = "10 crores"


# Child class inherits parent class
class Regexsoftware(RegexEduhub):
    student = 1000


print("*******************************")


# ================================================================
# 2️⃣ SINGLE INHERITANCE WITH METHODS + super()
# ---------------------------------------------------------------

class Tatamotors:
    employee = 5000
    revenue = "500 crores"

    def info(self):
        print("This is Tata motors class",
              "employee =", self.employee,
              "profit =", self.revenue)


class tataharier(Tatamotors):          # child inherits Tatamotors
    model = "Harrier"
    price = "20 lakhs"

    def infoharier(self):
        print("This is Tata Harrier class")
        super().info()     # accessing parent class method


t1 = tataharier()
t1.infoharier()


"""
📌 super()
- Used to access parent class methods OR constructor.
- Helps avoid rewriting parent code.
"""


print("*******************************")


# ================================================================
# 3️⃣ MULTILEVEL INHERITANCE
# Parent → Child → Grandchild
# ---------------------------------------------------------------

class customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def get_info(self):
        print("Getting info:", self.name, self.email, self.phone)


class driver(customer):   # driver inherits customer
    def __init__(self, a, b, c):
        super().__init__(a, b, c)   # calling parent constructor


d1 = driver("John", "john@example.com", "1234567890")
print(d1.name, d1.email, d1.phone)


"""
📌 MULTILEVEL
customer → driver → (next level possible)
"""


print("*******************************")


# ================================================================
# 4️⃣ MULTIPLE INHERITANCE
# Child inherits from TWO parents
# ---------------------------------------------------------------

class Father:
    car = "XUV700"

class Mother:
    house = "3 BHK Apartment"

class Child(Father, Mother):   # multiple inheritance
    name = "Akash"


c = Child()
print(c.name, c.car, c.house)


"""
📌 MULTIPLE INHERITANCE
- A class inherits from MANY parent classes.
"""


print("*******************************")


# ================================================================
# 5️⃣ HYBRID INHERITANCE
# Combination of multiple + multilevel
# ---------------------------------------------------------------

class School:
    def school_info(self):
        print("This is a school.")

class Teacher(School):
    def teacher_info(self):
        print("This is teacher class.")

class Student(School):
    def student_info(self):
        print("This is student class.")

class Monitor(Student, Teacher): 
    # hybrid → because student & teacher inherit from same parent
    pass


m = Monitor()
m.school_info()
m.student_info()
m.teacher_info()


"""


End of Notes.
"""
