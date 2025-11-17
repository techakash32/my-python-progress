for i in range(1,8):
    x=1
    for j in range(1,8-i):
        print("",end=" ")
    for k in range(1,i+1):
        if (i==3 or i==1 or i==5 or i==7):
            print("*",end=" ")
            x+=1   
    print()