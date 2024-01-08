import sys
import heapq
input = sys.stdin.readline
n,m = map(int, input().split())
INF = 1e9
arr = [[] for _ in range(n+1)]
k= int(input())
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a].append((b,c))
distance = [INF]*(n+1)

def dijk(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1],i[0]))

dijk(k)
for d in distance[1:]:
    if d == 1e9:
        print("INF")
    else:
        print(d)