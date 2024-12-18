import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
arr = list(map(int, input().split()))

q = deque([i for i in range(1,n+1)])
cnt = 0
while len(arr)>0:
    now = arr.pop(0)

    while True:
        if q[0] == now:
            q.popleft()
            break

        idx = q.index(now)
        ddx = len(q) - idx
        if idx < ddx:
            q.rotate(-idx)
            cnt+=idx
        else:
            q.rotate(ddx)
            cnt+=ddx
print(cnt)