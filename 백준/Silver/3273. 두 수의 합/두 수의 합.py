n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

lt = 0
rt = n-1
cnt = 0
while rt>lt:

    res = arr[lt] + arr[rt]
    if res == x:
        cnt+=1

    elif res >= x:
        rt -= 1
        continue
    lt +=1

print(cnt)