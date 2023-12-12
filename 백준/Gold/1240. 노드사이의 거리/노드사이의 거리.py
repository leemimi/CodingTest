from collections import deque
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
def bfs(start, end):
    q = deque()
    q.append((start,0))
    visited = [False]*(n+1)
    visited[start] = True
    while q:
        v,d = q.popleft()

        if v == end:
            return d

        for i, l in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append((i,d+l))



for i in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


for j in range(m):
    a,b = map(int,input().split())
    print(bfs(a,b))