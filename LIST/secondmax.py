list=[12,34,56,78,90,11,23,45]
max=0
secondmax=0
for i in range(len(list)):
    if list[i]>max:
        secondmax=max
        max=list[i]
    elif list[i]>secondmax and list[i]!=max:
        secondmax=list[i]

print("Second largest number is:",secondmax)
print("Largest number is:",max)