x=1
for i in range(1, 6):
    for j in range(1, 6-i):
            print(" ", end=" ")
    for k in range(i,i*2):
            print(k, end=" ")
    for l in range(i*2-2, i-1, -1):
            print(l, end=" ")

    print()