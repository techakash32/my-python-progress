for i in range(1,6):
    x=65
    for j in range(1,6-i):
        print("",end=" ")
    for k in range(i,i+5):
        print(chr(x),end=" ")
        x+=1    
    print()