import sys

input = sys.stdin.readline
from collections import deque
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indgree = [0]*(n+1)

for _ in range(m):
    tmp = []
    tmp = list(map(int, input().split()))
    c = tmp[0]
    for i in range(1,c):
        graph[tmp[i]].append(tmp[i+1])
        indgree[tmp[i+1]]+=1

q = deque()
res = []

for i in range(1,n+1):
    if indgree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    res.append(cur)
    for i in graph[cur]:
        indgree[i] -=1
        if indgree[i] == 0:
            q.append(i)
if len(res) != n:
    print(0)
else:
    for j in res:
        print(j)



