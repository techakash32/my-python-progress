list=[10,20,30,10,40,50,20,60]

uniquelist=[]
duplist=[]
for i in range(len(list)):
    curr=list[i]
    if curr not in uniquelist:
        uniquelist.append(curr)
    else:
        duplist.append(curr)
print(uniquelist,"Duplicate elements:",duplist)
    