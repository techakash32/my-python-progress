for i in range(1,6):
    x=1
    for j in range(1,6-i):
        print("",end=" ")
    for k in range(i,i+5):
        print("*",end=" ")
        x+=1    
    print()