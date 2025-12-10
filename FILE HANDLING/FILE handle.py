"""
======================================
📌 FILE HANDLING IN PYTHON (NOTES + EXAMPLES)
======================================

File handling is one of the most important parts of Python.
It allows you to **create, read, update, and delete** files.

Python provides a built-in function `open()` to work with files.

FORMAT:
open("filename", "mode")

Common Modes:
------------
'r'  → Read (default)
'w'  → Write (overwrite)
'a'  → Append
'x'  → Create (error if file exists)
'b'  → Binary mode
't'  → Text mode (default)
'r+' → Read + Write
'w+' → Write + Read (overwrite)
'a+' → Append + Read

Always close file after use using:
file.close()

OR use `with open()` which auto-closes the file.
"""


# 1️⃣ OPEN A FILE & READ CONTENT
# ------------------------------
# Modes: 'r' = read (file must exist)

file = open("data.txt", "r")
print(file.read())       # Read entire file
file.close()


# 2️⃣ READ LINE BY LINE
# ----------------------

file = open("data.txt", "r")
print(file.readline())   # Reads first line
print(file.readline())   # Reads next line
file.close()


# 3️⃣ READ ALL LINES AS LIST
# ---------------------------

file = open("data.txt", "r")
lines = file.readlines()
print(lines)      # ['line1\n', 'line2\n', ...]
file.close()


# 4️⃣ WRITE TO A FILE
# --------------------
# Mode: 'w' → overwrites entire file

file = open("data.txt", "w")
file.write("Hello Akash!\n")
file.write("Welcome to Python file handling.")
file.close()


# 5️⃣ APPEND TO A FILE
# ---------------------
# Mode: 'a' → adds new content at the end

file = open("data.txt", "a")
file.write("\nThis line is appended.")
file.close()


# 6️⃣ USING 'with open()' (BEST PRACTICE)
# ----------------------------------------
# It automatically closes the file.

with open("data.txt", "r") as f:
    content = f.read()
    print(content)


# 7️⃣ WRITE + READ TOGETHER
# --------------------------
# Mode: 'w+' → write then read (file is cleared)
# Mode: 'a+' → append then read

with open("sample.txt", "w+") as f:
    f.write("Python is amazing!")
    f.seek(0)           # Move cursor to start
    print(f.read())


# 8️⃣ CHECK IF FILE EXISTS
# -------------------------

import os

if os.path.exists("data.txt"):
    print("File exists!")
else:
    print("File not found!")


# 9️⃣ DELETE A FILE
# ------------------

import os
os.remove("sample.txt")    # Deletes file


"""
SUMMARY
-------
✔ open() is used to operate on files
✔ Modes: r, w, a, x, b, t, r+, w+, a+
✔ read(), readline(), readlines() for reading
✔ write(), append() for writing
✔ Use 'with open()' → closes file automatically
✔ os module helps in checking and deleting files

Python file handling is useful for:
➡ Data storage
➡ Logging
➡ Configuration files
➡ Machine learning datasets
➡ Automation scripts

End of Notes.
"""
