t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * (max(n+1, 4))
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    if n <= 3:
        print(dp[n])
        continue
    else:
        for i in range(4, n+1):
            dp[i] = dp[i-3] + dp[i-2]
    print(dp[n])
