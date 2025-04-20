import sys
input = sys.stdin.readline

import heapq
n,m = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for i in range(m):
    a,b,t = map(int, input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))
dist = [float('inf')] * n
arr[-1] = 0
def dijkstra(start):
    dist[start] = 0
    hp = []
    heapq.heappush(hp, (0, start))

    while hp:
        d, now = heapq.heappop(hp)
        if dist[now] < d:
            continue
        for nx, cost in graph[now]:
            cs = d + cost
            if dist[nx] > cs and arr[nx] == 0:
                dist[nx] = cs
                heapq.heappush(hp, (cs, nx))



dijkstra(0)
print(dist[-1] if dist[-1] != float('inf') else -1)