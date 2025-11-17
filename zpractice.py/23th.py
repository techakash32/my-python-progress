list=[3,1,4,1,5,9,2]
max1=0
max2=0
for i in range(len(list)):
    if list[i]>max1:
        max2=max1
        max1=list[i]
    elif list[i]>max2 and list[i]!=max1:
        max2=list[i]
print(max2)
