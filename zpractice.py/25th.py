a="LeveL"
ans=0

for i in range(len(a)):
    j=(len(a)-1)-i
    if a[i]!=a[j]:
        ans=0
        break
    else:
        ans=1
if ans==1:
    print("pali")
else:
    print("not")
