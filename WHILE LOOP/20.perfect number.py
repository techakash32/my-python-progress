n=28
i=1
sum=0
while i<n:
    if n%i == 0:
        sum=sum+i
    i+=1
if sum == i:
    print("perfect")
else: 
    print("not perfect")