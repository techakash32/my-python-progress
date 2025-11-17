num=5
mylist=[]
for i in range(0,num):
    temp=[]
    for j in range(0,num-i):
        print("-",end="")
    for k in range(0,i+1):
        if k==0 or i==k:
            print(1,end=" ")
            temp.append(1)
        else:
            print("*",end=" ")
            temp.append("*")

    mylist.append(temp)
    print(" ")
    print(mylist)              