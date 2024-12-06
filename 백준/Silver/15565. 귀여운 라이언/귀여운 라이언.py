n,k = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
rt = k-1
res = n+1

tmp = []

for i in range(n):
    if arr[i] == 1:
        tmp.append(i)


if len(tmp) < k:
    print(-1)
    exit(0)
while True:
    lengths = tmp[rt] - tmp[lt] +1
    res = min(res, lengths)
    if rt == len(tmp)-1:
        break

    lt+=1
    rt+=1
print(res)