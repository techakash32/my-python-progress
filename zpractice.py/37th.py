s='aaabbbccc'
a=0
b=0
c=0
for i in s:
    if i=='a':
        a+=1
    elif i=='b':
        b+=1
    elif i=='c':
        c+=1
print(f"a{a}b{b}c{c}")