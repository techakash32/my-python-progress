words = ['red' ,'blue','green','blue', 'red']
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if words[i]==words[j]:
            words.pop(j)
            
print(words)