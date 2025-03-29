n,k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [10001]*(k+1)
dp[0] = 0

for coin in arr:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])