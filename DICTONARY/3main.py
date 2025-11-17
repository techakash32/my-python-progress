myaadhar={4050:"tusar",4050:"akash"}
myaadhar[4050] 
myaadhar[454546]="gaurav"     
myaadhar.pop(4050)      

#make diffternt key for one element:

mydic={}
for i in range(10,15):
    mydic[i]="akash"

#insert the element in dic:

d={}
data="abc"
for i in range(0,3):
    d[data[i]]=i
    print(i,data[i])
print(i,data[i],d)

#make different word same element:

data="hey RAM"
d={}
for i in data:
    d[i]=1
print(i,d)

#find vowel in the ditonary:

d={}
data="hey ramucem"
for i in data:
    if(i in "aeiou"):
        if i not in d:
             d[i]=1
        else:
            d[i]=d[i]+1
print(i,d)

#use in or not in:

d={10:"japan"}
print("old::",d)

if ("salary" in d):
    d["salary"] =d["salary"]+1
else:
    d["salary"]=500
print(d)

#list to dictonary

list=[1,3,5,7]
dic={}
for i in range(len(list)):
    dic[list[i]]=i
print(dic)

#sum problem

target=12
for i in list:
    x=target-i
print(target,i,x)

#

