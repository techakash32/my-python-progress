#oprator overloading: it is a unique feature of oops which allows us to define custom behavior for operators in user-defined classes.
"""
example:            __add__==> + operator
                   __sub__==> - operator
                   __mul__==> * operator
                   __div__==> / operator
                   __mod__==> % operator
                   __str__==> to string conversion
                   __gt__==> greater than operator
                   __lt__==> less than operator
                   __eq__==> equal to operator
                   __ne__==> not equal to operator
                   __init__==> constructor
                   __del__==> destructor

"""

class Twoadd:
    def info(self):
        print("heyy user")
    def __add__(self, object2):
        print("Overloading + operator")

t1=Twoadd()
t2=Twoadd()
object3=t1 + t2  # it will call the __add__ method


