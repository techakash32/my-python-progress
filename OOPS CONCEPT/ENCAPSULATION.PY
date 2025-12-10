"""
===============================================================
📌 PYTHON ENCAPSULATION (NOTES + EXAMPLES)
===============================================================

Encapsulation = Binding data (variables) and methods (functions)
inside a class and can controlling access to them.

#ENCAPSULATION: ENCAPSULATION is one of the fundamental concepts in OOP.where we combined the varibale
two method together in a single class to provide data accessbiltity.

---------------------------------------------------------------
WHY ENCAPSULATION - ?
---------------------------------------------------------------

1. encapsulation is a fundamental OOP concept.
2. encapsulation helps in data hiding and restricting access
to certain components of an object.
3. it is also used to prevent unintended interference.
4. it also helps in bundling data and methods.
that operate on the data within a single unit (class).
5. It protects data from accidental modification and provides security.

===============================================================
#package = where we store multiple files and programs sothat we can reuse it. 

#subclass = it is a class which inherits the properties of another class.

#protected members =  are accessible within the same package and also available to all subclasses.
also have inheritance.

#private members = are accessible only within the class where they are defined.

#public members = are accessible from any other class.

---------------------------------------------------------------
TYPES OF ACCESS MODIFIERS (Python)
---------------------------------------------------------------
1️⃣ Public Members      → accessible everywhere ( var )
2️⃣ Protected Members   → accessible inside class & subclass ( _var )
3️⃣ Private Members     → accessible only inside class ( __var )

---------------------------------------------------------------
Why Encapsulation?
---------------------------------------------------------------
✔ Protects data  
✔ Prevents accidental changes  
✔ Controls variable access  
✔ Implements security in classes  
✔ Used in real projects (banking, login, APIs)

===============================================================
# 1️⃣ PUBLIC MEMBERS (Default)
===============================================================
"""

class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self.age = age         # public

s = Student("Akash", 22)
print(s.name)      # accessible
print(s.age)       # accessible


print("---------------------------------------------------------")
"""
===============================================================
# 2️⃣ PROTECTED MEMBERS (single underscore _ )
# Meaning: "use carefully" but still accessible
===============================================================
"""

class Company:
    def __init__(self):
        self._revenue = 500000     # protected variable

class Branch(Company):
    def show(self):
        print("Revenue from parent class:", self._revenue)

b = Branch()
b.show()
print(b._revenue)      # still accessible, but NOT recommended


print("---------------------------------------------------------")
"""
===============================================================
# 3️⃣ PRIVATE MEMBERS (double underscore __ )
# Meaning: fully private; cannot be accessed directly
===============================================================
"""

class Bank:
    def __init__(self):
        self.__pin = 1234     # private variable

    def show_pin(self):
        print("PIN (inside class):", self.__pin)

bank = Bank()
bank.show_pin()

# print(bank.__pin)         ❌ ERROR → cannot access directly

# Accessing private variable using name-mangling:
print("Accessing private via name-mangling:", bank._Bank__pin)


print("---------------------------------------------------------")
"""
===============================================================
# 4️⃣ PRIVATE METHODS (Same concept for functions)
===============================================================
"""

class Server:
    def __connect(self):              # private method
        print("Connecting to server...")

    def start(self):
        self.__connect()              # allowed inside class

s = Server()
s.start()

# s.__connect()      ❌ ERROR – cannot access outside


print("---------------------------------------------------------")
"""
SUMMARY
---------------------------------------------------------------
✔ Encapsulation = data hiding + access control  
✔ Public → accessible everywhere  
✔ Protected → internal/class + subclass  
✔ Private → only inside class  
✔ Private variables accessed using _ClassName__variable  
✔ Improves security & prevents accidental modification

END OF NOTES.
================================================================
"""