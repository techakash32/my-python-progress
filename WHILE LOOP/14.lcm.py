m=220
n=6

i=2
mn=1
while n>1 or m>1:
    if m%i == 0 or n%i == 0:
        if n%i == 0:
            n=n//i
        if m%i==0:
            m=m//i
        mn=mn*i
    else:
        i+=1
print(mn)
