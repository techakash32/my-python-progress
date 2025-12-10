'''
====================================================================
📌 PYTHON MRO (METHOD RESOLUTION ORDER) — NOTES + EXAMPLES + COMMENTS
====================================================================

DEFINITION:
-----------
MRO (Method Resolution Order) is the order in which Python searches
for a method or variable in a class inheritance hierarchy.

In simple words:
➡ When you call an object.method(), Python follows a fixed order
   to find that method in parent classes.

WHY DO WE NEED MRO?
-------------------
✔ To avoid confusion in multiple inheritance  
✔ To solve the “diamond problem”  
✔ To ensure predictable and consistent method lookup  
✔ To know which parent method Python will call  
✔ To maintain clean inheritance rules  

Python internally uses the **C3 Linearization Algorithm** to calculate MRO.

====================================================================
# HOW TO CHECK MRO?
# ---------------------------------------------------------------
1️⃣ ClassName.__mro__  
2️⃣ ClassName.mro()  
====================================================================
"""

# Example:
class A: pass
class B(A): pass
class C(B): pass

print(C.mro())   # Shows MRO order: [C, B, A, object]


print("------------------------------------------------------------")
"""
====================================================================
# 1️⃣ SINGLE INHERITANCE MRO
# ---------------------------------------------------------------
RULE:
Child → Parent → object

Simplest form of inheritance.
====================================================================
"""

class A:
    def show(self):
        print("Class A method")

class B(A):  # B inherits A
    pass

b = B()
b.show()    # Class A method (found in parent)

print(B.mro())  # [B, A, object]


print("------------------------------------------------------------")
"""
====================================================================
# 2️⃣ MULTIPLE INHERITANCE MRO
# ---------------------------------------------------------------
RULE:
Left Parent → Right Parent → Grandparents → object

Python uses C3 Linearization:
✔ Left parent is checked first
✔ Then right parent
✔ No class appears twice
====================================================================
"""

class A:
    def show(self):
        print("A class method")

class B:
    def show(self):
        print("B class method")

class C(A, B):   # Multiple inheritance
    pass

c = C()
c.show()        # A class method (because A is first in MRO)

print(C.mro())  # [C, A, B, object]


print("------------------------------------------------------------")
"""
====================================================================
# 3️⃣ DIAMOND PROBLEM (MRO SOLVES IT)
# ---------------------------------------------------------------
Structure:

        A
       / \
      B   C
       \ /
        D

Both B and C inherit A.  
D inherits B and C.

Which show() should D call?
➡ Python follows MRO to decide.
====================================================================
"""

class A:
    def show(self):
        print("A method")

class B(A):
    pass

class C(A):
    def show(self):
        print("C method")   # Overrides A

class D(B, C):  # Diamond shape
    pass

d = D()
d.show()       # C method (MRO chooses C before A)

print(D.mro())  # [D, B, C, A, object]


print("------------------------------------------------------------")
"""
====================================================================
SUMMARY OF MRO
====================================================================

✔ MRO determines how Python searches for methods/variables.

✔ Python uses:
   → C3 Linearization Algorithm  
   → Left-to-right rule  
   → No repeated classes  

✔ Use:
   → Class.mro()  
   → Class.__mro__  

✔ MRO helps in:
   • Multiple inheritance  
   • Removing confusion  
   • Predictable method lookup  
   • Avoiding ambiguity in diamond inheritance  

END OF NOTES.
"""

'''