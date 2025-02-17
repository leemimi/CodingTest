import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()
s,e = map(int,input().split())


def bfs(start,e, visited):
    q = deque()
    q.append((start, 0, str(start)))
    visited[start] = True
    while q:
        now, distance, going = q.popleft()
        
        if now == e:
            return distance, going
        for new in graph[now]:
            if not visited[new]:
                q.append((new, distance+1, going + ' '+ str(new)))
                visited[new] = True


visited= [False]*(n+1)
first, go = bfs(s,e, visited)
visited= [False]*(n+1)

for i in list(map(int, go.split())):
    visited[i] = True

visited[s]= False
visited[e]= False

print(first+bfs(e,s,visited)[0])