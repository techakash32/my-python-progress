n=145
temp=n
digit=0
total=0
while temp>0:
    digit=temp%10
    temp=temp//10

    fact=1
    i=1
    while i<=digit:
        fact=fact*i
        i+=1
    total=total+fact
if total==n:
    print("armstrong number")
else:
    print("not")