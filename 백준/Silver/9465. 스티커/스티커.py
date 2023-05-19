t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    for j in range(2):
        arr.append(list(map(int, input().split())))
    dp = [[0]*(3) for j in range(n)] # dp[0][2] = 0, 아무것도 고르지 않은 경우
    dp[0][0] = arr[0][0] # 윗줄 선택
    dp[0][1] = arr[1][0] # 아랫줄 선택
    for j in range(1, n):
        dp[j][0] = max(dp[j-1][1], dp[j-1][2]) + arr[0][j]
        dp[j][1] = max(dp[j-1][0], dp[j-1][2]) + arr[1][j]
        dp[j][2] = max(dp[j-1])
    print(max(dp[n-1]))
    arr.clear()