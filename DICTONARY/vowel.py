a="akash"
dic={"count":0}
for i in range(0,len(a)):
    if a[i] in "aeiou":
        dic["count"]=dic["count"]+1
        print(a[i])
print(dic["count"])