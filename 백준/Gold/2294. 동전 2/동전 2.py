n,k = map(int,input().split())
coin = []
for _ in range(n):
    c = int(input())
    coin.append(c)

dp = [10001]*(k+1)
dp[0] = 0
for c in coin:
    for i in range(c, k+1):
        dp[i] = min(dp[i],  dp[i-c]+1)
if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])