def solution(n, money):
    
    dp = [0]*(n+1)
    dp[0] = 1
    for m in money:
        for j in range(m,n+1):
            dp[j] += dp[j-m]

    
    return dp[-1]%1000000007