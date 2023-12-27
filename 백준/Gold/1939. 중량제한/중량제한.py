import sys
input=sys.stdin.readline
from collections import deque


n,m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

w1,w2 = map(int, input().split())
lt = 0
rt = 1000000000
ans = 0
def bfs(mid):
    q = deque()
    q.append(w1)
    visited[w1] = True

    while q:
        now = q.popleft()
        if now == w2:
            return True

        for node, cost in graph[now]:
            if not visited[node] and mid <= cost:
                q.append(node)
                visited[node] = True

    return False




while lt<=rt:
    mid = (lt+rt)//2
    visited = [False for _ in range(n+1)]

    if bfs(mid):
        ans = max(ans,mid)
        lt = mid+1
    else:
        rt = mid -1
print(ans)