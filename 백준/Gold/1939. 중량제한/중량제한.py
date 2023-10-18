import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
num1, num2 = map(int, input().split())


def bfs(weight):
    q =deque()
    q.append(num1)
    visited = [False]*(n+1)
    visited[num1] = True

    while q:
        x = q.popleft()

        for i,w in graph[x]:
            if not visited[i] and w >= weight:
                visited[i] = True
                q.append(i)
    if visited[num2] : return True
    else: return False

start = 1
end = 1000000000

res = 0
while start<=end:
    mid = (start+end)//2

    if bfs(mid):
        res = mid
        start = mid +1
    else:
        end = mid -1
print(res)