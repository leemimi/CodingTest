n,k = map(int, input().split())
arr = list(map(int, input().split()))

seq = [0] * (max(arr)+1)

lt = 0
rt = 0
res = 0
while rt < n:
    if seq[arr[rt]] <k :
        seq[arr[rt]] +=1
        rt +=1
    else:
        seq[arr[lt]] -= 1
        lt+=1
    res = max(res, rt - lt)
print(res)