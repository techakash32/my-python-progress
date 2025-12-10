"""
====================================
     ADVANCED NOTES ON lambda()
====================================
Python `lambda` is an anonymous, single-expression function.

Syntax:
    lambda arguments: expression

Key Points:
✔ No name required (anonymous)
✔ Must contain ONLY ONE expression
✔ Used when a short function is needed temporarily
✔ Often used with map(), filter(), sorted(), reduce(), list/dict operations
✔ Faster to write, but not always best for readability

------------------------------------------------------
1️⃣ Basic Example
------------------------------------------------------
square = lambda x: x * x
print(square(5))  # Output: 25

------------------------------------------------------
2️⃣ Lambda with Multiple Parameters
------------------------------------------------------
add = lambda a, b: a + b
print(add(10, 20))

------------------------------------------------------
3️⃣ Lambda with No Parameter
------------------------------------------------------
hello = lambda: "Hello World"
print(hello())

------------------------------------------------------
4️⃣ Lambda Inside Data Structures
------------------------------------------------------
funcs = [lambda x: x + 10, lambda x: x * 2, lambda x: x ** 2]

for f in funcs:
    print(f(5))    # Output: 15, 10, 25

------------------------------------------------------
5️⃣ Lambda Used in Sorting
------------------------------------------------------
data = [("Akash", 23), ("Rohan", 19), ("Gaurav", 30)]

# Sort by age
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

# Sort by name
sorted_name = sorted(data, key=lambda x: x[0])
print(sorted_name)

------------------------------------------------------
6️⃣ Lambda with Conditional Expression
------------------------------------------------------
status = lambda age: "Adult" if age >= 18 else "Minor"
print(status(17), status(19))

------------------------------------------------------
7️⃣ Lambda Inside Higher Order Functions (map, filter, reduce)
------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6]

mapped = list(map(lambda x: x * 2, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers))

print(mapped)
print(filtered)

------------------------------------------------------
8️⃣ reduce() with lambda (Functional Programming)
------------------------------------------------------
from functools import reduce

total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)

------------------------------------------------------
9️⃣ Lambda with *args and **kwargs (Trick)
------------------------------------------------------
# YES, lambda supports variable arguments
combine = lambda *args: sum(args)
print(combine(1,2,3,4,5))

info = lambda **kwargs: kwargs
print(info(name="Akash", age=21))

------------------------------------------------------
🔟 Nested Lambda (Currying) — Interview Favorite
------------------------------------------------------
adder = lambda a: lambda b: a + b
add10 = adder(10)
print(add10(5))  # 15

------------------------------------------------------
⚠️ What lambda cannot do:
------------------------------------------------------
❌ No multiple statements
❌ No loops directly inside
❌ No annotations or docstrings

Example (Invalid):
    lambda x: (y=x+5; print(y))  --> SyntaxError


# =========================
#       MCQ QUESTIONS
# =========================

# Q1: lambda x: x + 5 is:
# A) Named function   B) Anonymous function ✔   C) Loop   D) Class

# Q2: Which is correct?
# A) lambda x: return x*x
# B) lambda x: print(x)
# C) lambda x: x*x ✔

# Q3: Can lambda have multiple expressions?
# A) Yes   B) No ✔   C) Only in Python 3   D) Only with map

# Q4: Output of this:
l = lambda x, y=5: x+y
print(l(10))
# A) Error   B) 5   C) 10   D) 15 ✔

# Q5: Output of this:
func = (lambda x: (lambda y: x+y))(10)
print(func(5))
# A) 5   B) 10   C) 15 ✔   D) Error


# 🎯 Summary:
""""""
- `lambda` creates anonymous single-expression functions.
- Used with map(), filter(), reduce(), sorted(), and functional programming.
- Can accept *args, **kwargs, and support currying.
- Not suitable for long or complex logic — use normal def instead.
"""