list=[123,456,789,101]
max=0
min=0
for i in range(len(list)):
    curr=list[i]
    if curr>max:
        max=curr
    if curr<min or min==0:
        min=curr    

print("The maximum is:",max)
print("The minimum is:",min)