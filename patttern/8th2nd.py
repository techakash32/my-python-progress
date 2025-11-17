for i in range(1,6):
    x=65
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(1,7-i):
        print(chr(x),end=" ")
        x+=1
    print()