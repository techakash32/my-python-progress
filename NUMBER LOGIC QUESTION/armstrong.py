num=153
temp=num
count=0

while temp>0:
    temp//=10
    count+=1
print(count)

temp=num
digit=0
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**count
    temp=temp//10
    print(digit)
print(sum)

if sum==num:
    print("armstrong")
else:
    print("not armstrong")