n=10
i=2
j=1
count=0
while i<=n:
    while j<=i:
            if i%j == 0:
                count +=1
                i+=1
    if count == 2:
        print(i)
j+=1
            