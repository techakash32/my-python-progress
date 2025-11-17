n=100
i=2
while i<=n:
    count=0
    j=1
    while j<=i:
            if i%j == 0:
                count +=1
            j+=1
    if count == 2:
        print(i)
    i+=1
            