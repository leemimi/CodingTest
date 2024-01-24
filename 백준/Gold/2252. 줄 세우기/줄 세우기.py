import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indgree = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indgree[b]+=1

q = deque()
res = []
for i in range(1,n+1):
    if indgree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    res.append(cur)
    for j in graph[cur]:
        indgree[j] -=1
        if indgree[j] == 0:
            q.append(j)

print(*res)
