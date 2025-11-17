n=15
a=1
b=0
ans=0

for i in range(15,1,-1):
    ans=a+b

    print(b)
    a=b
    b=ans
print(ans)