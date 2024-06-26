import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())

def dijkstar(s):
    if s == end:
        return

    q = []
    heapq.heappush(q,(0,s))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+ i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


distance[start] = 0
dijkstar(start)
print(distance[end])