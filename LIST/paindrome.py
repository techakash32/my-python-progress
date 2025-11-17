list=[12,34,45,34,12]
end=len(list)-1
x=0
i=0
while(i<len(list)):
    if list[i]!=list[end]:
        x=1
        break
    print(i,end)
    print(i,list[i],list[end])
    end-=1
    i+=1
if x==0:
    print("palindrome")
else:
    print("not a vaild palindrome")
