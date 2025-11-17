for i in range(1,7):
    for j in range(1,1+i):
        print("",end=" ")
    for k in range(1,8-i):
        if k==1 or k==7-i or i==1:
                print("*",end=" ")
        else:
            print(" ",end=" ")
        
    print()