x="akashnagar"
count=0
countx=0
for i in range(len(x)):
    if x[i] in 'aeiou':
        count+=1
        print(i,x[i],"vowel")
    else:
        countx+=1
        print(i,x[i],"consonant")
print("vowel",count)
print("consonent",countx)
