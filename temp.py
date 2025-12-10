a="anagram"
b="nagaram"
x=0
y=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]==b[j]:
            x+=1
        else: 
            y+=1
if x==len(a):
    print("yes")
else:
    print("no")