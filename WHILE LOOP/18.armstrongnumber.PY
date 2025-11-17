n = 153
temp=n
count=0
while(temp>0):
    count+=1
    temp=temp//10

temp=n
sum=0
digit=0
while temp>0:
    digit = temp % 10
    sum =sum+digit ** count
    temp =temp//10
if sum == n:
    print("ARNSTRONG NUMBER")
else:
    print("NOT ARMSTRONG NUMBER")