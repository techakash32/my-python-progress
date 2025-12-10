# ================================================================
# ⚡ OPERATOR OVERLOADING IN PYTHON
# ---------------------------------------------------------------
# Operator overloading allows user-defined classes to define how
# operators (+, -, *, >, ==, etc.) behave with class objects.
#
# Example:
#     __add__()  →  +
#     __sub__()  →  -
#     __mul__()  →  *
#     __truediv__() → /
#     __mod__()  →  %
#     __str__()  →  string representation
#     __gt__()   →  >
#     __lt__()   →  <
#     __eq__()   →  ==
#     __ne__()   →  !=
#     
#     __del__()  →  destructor
# ---------------------------------------------------------------
# Python internally maps operators to special methods (dunder methods).
# By defining these methods, we can customize operator behavior.
# ================================================================


class TwoAdd:
    def info(self):
        print("Hey user!")

    # Overloading the + operator
    def __add__(self, other):
        print("Overloading + operator between two TwoAdd objects")
        return "Addition operation completed"


t1 = TwoAdd()
t2 = TwoAdd()

# This will automatically call t1.__add__(t2)
result = t1 + t2

print("Returned from __add__:", result)
