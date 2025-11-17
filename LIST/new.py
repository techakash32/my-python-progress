list = [2, 7, 11, 15]
target = 17

for i in range(len(list)):

    for j in range(i + 1, len(list)):

        if list[i] + list[j] == target:

            print( list.index(list[i])+1, list.index(list[j])+1 )

            