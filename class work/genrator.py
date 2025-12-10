def func(n):
    a=1
    b=0
    for i in range(n,0,-1):
        ans=a+b
        yield b
        a=b
        b=ans
x=func(10)
print(list(x))
