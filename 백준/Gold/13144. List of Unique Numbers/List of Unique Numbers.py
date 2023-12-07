n = int(input())
arr = list(map(int, input().split()))

lt = 0
rt = 0
res = 0
ch = [0]*1000001
while rt <n:
    if not ch[arr[rt]]:
        ch[arr[rt]] = 1
        rt+=1
        res += (rt-lt)
    else:
        ch[arr[lt]] = 0
        lt+=1
print(res)