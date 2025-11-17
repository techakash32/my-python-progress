if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    count=1
for i in arr:
    if i==(" "):
        count+=1
print(count)