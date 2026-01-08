import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[b].append(a)

ans = [0]*(n+1)
def bfs(start):
    q = deque([start])
    visited = [False]*(n+1)
    visited[start] = True
    cnt = 1

    while q:
        cur = q.popleft()
        for nx in arr[cur]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
                cnt+=1
    return cnt
mx = 0
res = []
for i in range(1, n+1):
    c = bfs(i)
    if c > mx:
        mx = c
        res = [i]
    elif c == mx:
        res.append(i)
print(*res)