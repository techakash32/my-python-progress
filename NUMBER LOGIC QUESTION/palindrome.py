n=1221
temp=n
rev=0
digit=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp == rev:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")