names = ["anna", "Bob", "ALICE", "Tim"]
list1=[]
for i in names:
    new_name = ""
    for j in range(len(i)):
        char=i[j]
        if j==0:
            if 'a' <= char <= 'z':
                new_name=new_name+chr(ord(char)-32)
            else:
                new_name=new_name+char
        else:
            if 'A' <=char <= 'Z':
                 new_name += chr(ord(char) + 32)
            else:
                new_name=new_name+char
    list1=list1+[new_name]
print(list1)