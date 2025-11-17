count=0
for n in range(2,8):
    c={"count":0}
    for i in range(1,n+1):
        if n%i==0:
            c["count"] += 1
            

    if c["count"]==2:
        count+=1
        print("prime",n)
        print(count)
