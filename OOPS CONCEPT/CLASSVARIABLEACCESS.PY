"""
====================================================================
📌 CLASS VARIABLES — ACCESSING & MODIFYING (NOTES + EXAMPLES)
====================================================================

Class variables:
---------------------------------------------------------------------
✔ Shared by ALL objects  
✔ Stored inside the class  
✔ Changing class variable → affects every object ( unless overridden )

Instance variables:
--------------------------------------------------------------------
✔ Unique to each object  
✔ Created using self.variable  
✔ Changing instance variable → affects only that object  

"""


print("*******************************")


# 1️⃣ CASE 1: MODIFYING INSTANCE VARIABLE (not class variable)
# ------------------------------------------------------------

class valuecounts:
    x = 0   # class variable

    def __init__(self):
        self.x = self.x + 1   # modifies instance variable


"""
👉 Here:
self.x looks for instance variable first.
If not found, it reads class variable value (0), then creates new instance variable x.
Class variable remains unchanged.
"""

v1 = valuecounts()
print(v1.x)     # 1 (instance-level)

v2 = valuecounts()
print(v2.x)     # 1 (again instance-level, class x not changed)


print("*******************************")


# 2️⃣ CASE 2: MODIFYING CLASS VARIABLE USING CLASS NAME
# -----------------------------------------------------

class valuecounts:
    x = 0   # class variable

    def __init__(self):
        valuecounts.x = valuecounts.x + 1
        # modifies class variable directly


"""
👉 Here:
We modify class variable using class name:
valuecounts.x

So every object sees UPDATED value.
"""

v3 = valuecounts()
print(v3.x)   # 1

v4 = valuecounts()
print(v4.x)   # 2

v5 = valuecounts()
print(v5.x)   # 3


print("*******************************")


"""
SUMMARY
-------
✔ self.x → creates or modifies INSTANCE variable  
✔ ClassName.x → modifies CLASS variable  
✔ Class variables are shared among all objects  
✔ Instance variables are unique per object  
✔ Changing class variable affects all objects immediately  
✔ Changing instance variable affects only that object  

End of Notes.
"""
