def solution(land):
    answer = 0

    dp = [[0]*len(land[0]) for _ in range(len(land))]
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for k in range(1,len(land)):
        dp[k][0] = max(dp[k-1][1],dp[k-1][2],dp[k-1][3])+land[k][0]
        dp[k][1] = max(dp[k-1][0],dp[k-1][2],dp[k-1][3])+land[k][1]
        dp[k][2] = max(dp[k-1][1],dp[k-1][0],dp[k-1][3])+land[k][2]
        dp[k][3] = max(dp[k-1][1],dp[k-1][2],dp[k-1][0])+land[k][3]
    return max(dp[len(land)-1])