import sys
input = sys.stdin.readline

n,L = map(int, input().split())
arr = []
for _ in range(n):
    a,b = map(int, input().split())
    arr.append((a,b))

arr.sort(key=lambda x:x[0])
cur = arr[0][0]
res = 0
for start, end in arr:
    if start > cur:
        cur = start
    diff = end - cur

    if diff % L == 0:
        cnt = diff//L
        cur = end
    else:
        cnt = diff//L +1
        cur = end + (L- (diff%L))
    res += cnt
print(res)