for i in range(1,10):
    for j in range(1,11-i):
        print("",end=" ")
    for k in range(1,1+i):
        print("*",end="")
    print()
for i in range(2,10):
    for j in range(1,1+i):
        print("",end=" ")
    for k in range(1,11-i):
        print("*",end="")
    print()
