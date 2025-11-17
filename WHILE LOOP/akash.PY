n=1
digit=0
sum=0
count =0
rev=0
temp=n
pro=1
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    sum=sum+digit
    pro =pro*digit
    count+=1
    temp=temp//10
if rev == n:
    print("palindrome")
else:
    print("not plaindrome")
temp=n
if temp%sum == 0:
    print("harshad number")
else:
    print("not harshad number")
if sum == pro:
    print("spy")
else:
    print("not spy")
if sum**2 == temp:
    print("neon number")
else:
    print("not a neon number")
print(sum)
print(count)
print(rev)

temp=n
sum_arm=0

while temp>0:
    digit=temp%10
    sum_arm=sum_arm+digit**count
    temp=temp//10
if sum_arm == n:
    print("armstrong")
else:
    print("not armstrong")

temp=n
i=1
sumer=0
while i<temp:
    if temp%i == 0:
        sumer=sumer+i
    i+=1
if sumer == temp:
    print("perfect number")
else:
    print("not perfect")
