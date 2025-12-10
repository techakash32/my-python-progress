'''
====================================================================
📌 PYTHON LIST — SHALLOW COPY vs DEEP COPY (NOTES + EXAMPLES)
====================================================================

In Python, when we copy lists, they do NOT always create new memory.
Some copies only copy the reference, not the actual data.

To understand this, we study:
✔ Shallow Copy  
✔ Deep Copy  

WHY DO WE NEED THIS?
--------------------
✔ To avoid accidental modification of original lists  
✔ To properly duplicate nested lists  
✔ To control memory usage  
✔ To understand how Python stores mutable objects  

====================================================================
# 1️⃣ SHALLOW COPY
# ---------------------------------------------------------------
DEFINITION:
Shallow Copy creates a new list, but **inner elements still share
the same memory**.

Meaning:
✔ Outer list is new  
✔ Inner/nested lists are NOT copied  
✔ If nested data is changed, both lists change  

WAYS TO DO SHALLOW COPY:
-------------------------
1. list.copy()
2. list slicing → new_list = old_list[:]
3. copy.copy()

====================================================================
import copy

lst1 = [1, 2, [3, 4]]
lst2 = copy.copy(lst1)   # shallow copy

lst2[2][0] = 100   # modifying nested list

print(lst1)   # → [1, 2, [100, 4]]  (changed)
print(lst2)   # → [1, 2, [100, 4]]

====================================================================
# 2️⃣ DEEP COPY
# ---------------------------------------------------------------
DEFINITION:
Deep Copy creates a **completely independent** copy of both:
✔ outer list  
✔ all nested lists  

Meaning:
✔ Changing nested values will NOT affect the original list.

HOW TO DO DEEP COPY:
--------------------
→ Using: copy.deepcopy()
====================================================================
import copy

lst1 = [1, 2, [3, 4]]
lst2 = copy.deepcopy(lst1)

lst2[2][0] = 200

print(lst1)   # → [1, 2, [3, 4]]  (unchanged)
print(lst2)   # → [1, 2, [200, 4]]

'''