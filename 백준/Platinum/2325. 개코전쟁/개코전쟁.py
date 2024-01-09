import sys
input = sys.stdin.readline
import heapq
INF = 1e9
n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))
visited = [[] for _ in range(n+1)]
dis = [INF]*(n+1)

def dijk(start):
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0
    visited[start] = [start]
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in arr[now]:
            if dist+i[1] < dis[i[0]]:
                visited[i[0]] = visited[now]+[i[0]]
                dis[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1],i[0]))
    return visited

def dijk2(s,e):
    distence = [INF]*(n+1)
    distence[1] = 0

    q = []
    heapq.heappush(q,(0,1))

    while q:
        d,now = heapq.heappop(q)

        if distence[now] < d:
            continue
        for i in arr[now]:
            if now == s and i[0] == e:
                continue
            elif now == e and i[0] == now:
                continue
            cost = d+i[1]

            if cost < distence[i[0]]:
                distence[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distence


d = dijk(1)
ans = 0

for i in range(len(d[n])-1):
    ans = max(ans, dijk2(d[n][i], d[n][i+1])[n])
print(ans)