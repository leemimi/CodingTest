import sys
input = sys.stdin.readline
import heapq
INF = sys.maxsize
n,m, k = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

dp = [[INF for _ in range(k+1)] for _ in range(n+1)]
dp[1] = [0 for _ in range(k+1)]

q = []
heapq.heappush(q, (0,1,0))

while q:
    dist, now, cover = heapq.heappop(q)
    if dp[now][cover] < dist:
        continue
    for next_node, next_cost  in arr[now]:
        cost = next_cost + dist
        if cost < dp[next_node][cover]:
            dp[next_node][cover] = cost
            heapq.heappush(q, (cost, next_node, cover))

        if cover < k:
            cost = dist
            if cost < dp[next_node][cover+1]:
                heapq.heappush(q, (cost, next_node, cover+1))
                dp[next_node][cover + 1] = cost

print(min(dp[n]))