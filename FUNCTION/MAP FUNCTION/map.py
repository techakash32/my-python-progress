"""
==============================
  ADVANCED NOTES ON map()
==============================
Python map() is a built-in higher order function used to apply a function to every element of an iterable.
It returns a **map object (iterator)** which is memory efficient.

Syntax:
    map(function, iterable1, iterable2, ...)

Key Points:
✔ map does NOT execute function immediately — it generates values lazily.
✔ Works with multiple iterables (parallel processing).
✔ map result must be converted using list(), tuple(), set(), etc.
✔ Faster than for-loop in many cases.
✔ Common in functional programming + interview questions.

------------------------------------------------------
1️⃣ Basic Example
------------------------------------------------------
def square(num):
    return num * num

result = map(square, [1, 2, 3, 4])
print(list(result))   # [1, 4, 9, 16]


------------------------------------------------------
2️⃣ map() with lambda (Most common)
------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
double = list(map(lambda x: x * 2, numbers))
print(double)   # [2, 4, 6, 8, 10]


------------------------------------------------------
3️⃣ map() with Multiple Iterables
------------------------------------------------------
a = [1, 2, 3]
b = [10, 20, 30]

result = list(map(lambda x, y: x + y, a, b))
print(result)   # [11, 22, 33]


------------------------------------------------------
4️⃣ Using map() with Built-In Functions
------------------------------------------------------
words = ["python", "map", "function"]
lengths = list(map(len, words))
print(lengths)  # [6, 3, 8]


------------------------------------------------------
5️⃣ Comparing map() vs for-loop vs List-Comprehension
------------------------------------------------------
# Using for-loop
out1 = []
for i in numbers:
    out1.append(i * 2)

# Using map
out2 = list(map(lambda x: x * 2, numbers))

# Using List Comprehension (Pythonic)
out3 = [x * 2 for x in numbers]

print(out1, out2, out3)

# List comprehension is more readable, but map is faster when using built-in functions.


------------------------------------------------------
6️⃣ map() with None (Python 2 feature, removed in Python 3)
------------------------------------------------------
# This used to group elements like zip() — ❌ NOT available in Python 3.


------------------------------------------------------
7️⃣ map() with type conversion (Real-Life Use)
------------------------------------------------------
data = ["10", "20", "30"]
converted = list(map(int, data))
print(converted)   # [10, 20, 30]


------------------------------------------------------
8️⃣ map() + filter() + lambda (Chaining)
------------------------------------------------------
data = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, data)))
print(result)  # [4, 16, 36]


------------------------------------------------------
9️⃣ Memory Behavior (Important MCQ Topic)
------------------------------------------------------
# map() returns an iterator → values are generated on demand.
# This saves memory when processing large datasets.

import sys
big_map = map(lambda x: x * 2, range(1000000))
print(sys.getsizeof(big_map))     # Very small size → lazy evaluator

# list(big_map) would take large memory.


------------------------------------------------------
🔟 map() with User-Defined Functions Inside Data Structures
------------------------------------------------------
def add10(x): return x + 10

def sub5(x): return x - 5

ops = [add10, sub5, lambda x: x * 2]

for f in ops:
    print(f"Applying {f.__name__ if hasattr(f,'__name__') else 'lambda'}:", list(map(f, [1,2,3])))


------------------------------------------------------
Bonus: map() with strings (Trick Question)
------------------------------------------------------
result = list(map(str.upper, "python"))
print(result)  # ['P','Y','T','H','O','N']

"""

# =========================
#       MCQ QUESTIONS
# =========================

# Q1: map() returns?
# A) List   B) Tuple   C) Iterator ✔   D) Generator

# Q2: Output of list(map(None, [1,2,3])) in Python3?
# A) [1,2,3]  B) Error ✔  C) (None,None,None)

# Q3: map(lambda x,y: x+y, [1,2], [3,4,5]) → output?
# A) [4,6,5]  B) Error  C) [4,6] ✔

# Q4: Which is fastest for math operations?
# A) for-loop  B) map() with built-in function ✔  C) List comprehension


# 🎯 Summary:
"""
- map() applies a function to iterable items.
- Fastest when used with built-in functions.
- Returns an iterator → memory efficient.
- Works with multiple iterables in parallel.
- Best used when readability is required in functional programming.
"""