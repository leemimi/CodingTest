n,m = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
rt = 1

cnt = 0

while rt <= n and lt<=rt:
    res = arr[lt:rt]
    tmp = sum(res)
    if tmp == m :
        cnt+=1
        rt +=1
    elif tmp > m:
        lt += 1
    else:
        rt+=1
print(cnt)