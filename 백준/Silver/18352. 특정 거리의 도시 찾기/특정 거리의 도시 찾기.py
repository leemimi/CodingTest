import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = 1+dist
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost, i))
                



dijkstra(x)
flag = False
for i in range(1,n+1):
    if distance[i] == k:
        flag = True
        print(i)
if not flag:
    print(-1)