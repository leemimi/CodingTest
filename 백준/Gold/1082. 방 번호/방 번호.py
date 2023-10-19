n = int(input())
arr = list(map(int,input().split()))
m = int(input())

dp = [0]*(m+1)

for i in range(n-1,-1,-1):
    r = arr[i]
    for j in range(r, m+1):
        dp[j] = max(dp[j-r]*10+i, i, dp[j])
print(dp[m])