"""
=====================================
    ADVANCED PYTHON EXCEPTION HANDLING
=====================================
Exception handling allows a program to continue execution even after an error occurs.
It improves code stability, avoids crashes, and helps debugging.

Keywords:
    try, except, else, finally, raise, assert

------------------------------------------------------------
1️⃣ try & except (Basic Error Handling)
------------------------------------------------------------
try:
    a = 100
    try:
        b = 10
        print(a / b)
    except:
        print("Inner error occurred")

    a + "gnkh"   # TypeError
    print("This line won't execute if error occurs above")

except Exception as e:
    print("Error is:", e)

# Output explanation:
# First division runs fine, then TypeError occurs.
# Outer except catches and prints the error.


------------------------------------------------------------
2️⃣ try, except, else (Else only runs if no error occurs)
------------------------------------------------------------
try:
    a = 100
    a + "dfgbm"   # Error occurs
    print("Output here")
except Exception as e:
    print("Error =", e)
else:
    print("This will execute only if no exception occurs")


------------------------------------------------------------
3️⃣ try, except, finally (finally always executes)
------------------------------------------------------------
try:
    a = 100
    print("Code executed successfully")
except Exception as e:
    print("Exception occurred:", e)
finally:
    print("Finally block executed — always runs (cleanup)")


------------------------------------------------------------
4️⃣ raise (Manually throw an exception)
------------------------------------------------------------
account = 15000
amount = 4000

try:
    if amount >= account:
        print("Account eligible")
    else:
        raise ValueError("Balance too low for operation")
except Exception as e:
    print("Error:", e)


------------------------------------------------------------
5️⃣ Multiple Except Clauses
------------------------------------------------------------
try:
    x = int("hello")  # ValueError
except TypeError:
    print("Type error occurred")
except ValueError:
    print("Value error occurred")
except Exception:
    print("Some other error occurred")


------------------------------------------------------------
6️⃣ Catching Specific Exceptions (Best Practice)
------------------------------------------------------------
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")


------------------------------------------------------------
7️⃣ Using `assert` Statement (Debugging)
------------------------------------------------------------
age = 17
try:
    assert age >= 18, "User not eligible"
    print("Access granted")
except AssertionError as e:
    print("Assertion failed:", e)


------------------------------------------------------------
8️⃣ Custom Exception Class (Interview Level)
------------------------------------------------------------
class LowBalanceError(Exception):
    pass

try:
    balance = 200
    withdraw = 500
    if withdraw > balance:
        raise LowBalanceError("Balance too low to withdraw")
    print("Withdraw successful")
except LowBalanceError as e:
    print("Custom Exception:", e)


------------------------------------------------------------
9️⃣ Best Practices
------------------------------------------------------------
✔ Catch specific exceptions
✔ Keep except block meaningful
✔ Use custom exceptions for large projects
✔ Always clean up resources in `finally`
✔ Avoid empty except blocks


# ==============================
# MCQ QUESTIONS (INTERVIEW TYPE)
# ==============================

# Q1: Which block always executes?
# A) try   B) except   C) else   D) finally ✔

# Q2: What does `raise` do?
# A) Ignore exception   B) Manually trigger an exception ✔
# C) Fix exception      D) Exit program

# Q3: Output?
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
finally:
    print("Done")

# Output → Error
#            Done ✔

# Q4: assert age >= 18 triggers?
# A) TypeError   B) AssertionError ✔   C) NameError

# Q5: Which is correct?
# A) except: only catches one type of error
# B) except Exception: catches all types ✔


# 🎯 Summary:
""""""""
- Exception handling prevents program crashes & handles errors safely
- `try` tests code, `except` handles errors
- `else` runs only if no error occurs
- `finally` ALWAYS executes (cleanup, file close)
- `raise` triggers manual error, supports custom exceptions
- Best practice → catch specific exceptions first
"""