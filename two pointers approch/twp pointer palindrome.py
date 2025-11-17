n = 'namman'
i=0
a=False
x=(len(n)-1)
while i<len(n):
    if n[i] != n[x]:
        a=True
        break
    i+=1
    x-=1
if a == True:
    print("not palidrome")
else:
    print("palindrome")