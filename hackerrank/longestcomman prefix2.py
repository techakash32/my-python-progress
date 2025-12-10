x=['flight','float','flse','fly','flow','flower']
x.sort()
first=x[0]
last=x[-1]
result=""
for i in range(min(len(first),len(last))):
    if first[i]==last[i]:
        result+=first[i]
    else:
        break
print(result)