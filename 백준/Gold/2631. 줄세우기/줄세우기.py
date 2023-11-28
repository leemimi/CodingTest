n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
dp = [0]*(n+1)
cnt = 0
for i in range(1,n+1):
    for j in range(1,i):
        if arr[i] > arr[j]:
            cnt = max(cnt, dp[j])
    dp[i] = cnt+1
    cnt = 0
print(n-max(dp))