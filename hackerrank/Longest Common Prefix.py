lst=['flower','flow','flight','flop','flourish']
prefix=''
for i in lst:
    if len(i)<len(prefix) or prefix=='':
        prefix=i
print(prefix)
need=len(lst)
count=0
result=''
for i in range(len(prefix)):
    count=0
    for j in lst:
        if prefix[i]==j[i]:
            count+=1
    if count==need:
        result+=prefix[i]
    else:
        break
print(result)