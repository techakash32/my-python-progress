list=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(len(list)):
    curr=list[i]
    sum=sum+curr
print("The sum is:",sum)
list.append(sum)
print("The new list is:",list)