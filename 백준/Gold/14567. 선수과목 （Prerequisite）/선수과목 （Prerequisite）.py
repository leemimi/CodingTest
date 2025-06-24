import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
degree = [0]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    degree[b] +=1
answer = [1]*(n+1)
q = deque()
res = []
for i in range(1,n+1):
    if(degree[i]==0):
        q.append(i)
        answer[i] = 1

for i in range(1,n+1):
    now = q.popleft()
    res.append(now)

    for nx in graph[now]:
        degree[nx] -=1
        if degree[nx]==0:
            q.append(nx)
        answer[nx] = answer[now]+1

print(*answer[1:])