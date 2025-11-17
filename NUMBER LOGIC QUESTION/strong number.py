n=145
temp=n
digit=0
fac=1
total=0
while n>0:
    digit=n%10
    n=n//10
    print(digit)

    fact=1
    i=1
    while i<=digit:
        fact=fact*i
        i+=1
    total =total+fact
if total == temp:
        print(temp, "is a Strong Number")
else:
        print("not")



