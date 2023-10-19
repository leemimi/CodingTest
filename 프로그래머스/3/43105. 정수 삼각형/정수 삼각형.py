def solution(triangle):
    answer = 0
    dp =[ [0]*i for i in range(1,len(triangle)+1)]
    dp[0] = triangle[0]
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif i == j:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
            
  
    
    return max(dp[-1])