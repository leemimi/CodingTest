n = int(input())
arr=[0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    dp[i] = arr[i]
    for j in range(i):
        if(arr[i] > arr[j]):
            dp[i] = max(dp[i], dp[j]+arr[i])
print(max(dp))