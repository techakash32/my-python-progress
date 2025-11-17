n=7
i=2
a=False

while(i<=(n-1)):
    if n%i == 0:
        a=True
        break
    i+=1
if a==True:
    print("not prime")
else:
    print("prime")