N,M = map(int, input().split())
arr = list(map(int, input().split()))
pset = set()

for i in range(M):
    pset.add(arr[i])
    for j in range(i+1,M):
        pset.add(arr[i]+arr[j])


INF = float('inf')
dp = [INF]*(N+1)
dp[0] = 0

for p in pset:
    for i in range(p,N+1):
        dp[i] = min(dp[i], dp[i-p]+1)

print(dp[N] if dp[N] != INF else -1)