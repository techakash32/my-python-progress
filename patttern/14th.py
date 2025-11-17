for i in range(1,9):
    for j in range(1,i+1):
        print("",end=" ")
    for k in range(1,9-i):
        if(i==1 or i==3 or i==5 or i==7):
            print("*",end=" ")
    print()