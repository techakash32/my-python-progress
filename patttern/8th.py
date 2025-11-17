for i in range(1,6):
    x=1
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(1,7-i):
        print(x,end=" ")
        x+=1
    print()