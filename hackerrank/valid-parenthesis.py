s='([{()}])'
var=[]
a=1
for ch in s:
    if ch=="(" or ch=="[" or ch == "{":
        var.append(ch)
        
    elif len(var)>0:
        if ch==")" and "(" == var.pop():
            a=0

        elif ch=="]" and "[" == var.pop():
            a=0

        elif ch=="}" and "{" == var.pop():
            a=0

        else:
            a=1
            break
    else:
        a=1
        break
if len(var)!=0 or a==1:
    print("invalid")
else:
    print("valid")