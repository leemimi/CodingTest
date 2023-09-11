n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

dp = [0]*(n+1)

dp[0] = arr[0]
if n > 1:
    dp[1] = arr[0] + arr[1]
if n > 2 :
    dp[2] = max(arr[0]+arr[2], arr[2]+arr[1], dp[1])
for i in range(3,n):
    dp[i] = max(dp[i-1], dp[i-3]+arr[i]+arr[i-1], dp[i-2]+arr[i])

print(max(dp))