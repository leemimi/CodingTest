import sys
input = sys.stdin.readline


n,k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

dp = [0]*(n+1)

dp[1] = 1
for i in range(1,n):
    for j in range(i+1,n+1):
        if dp[i] and (j-i)*(1+abs(arr[j]-arr[i]))<=k:
            dp[j] = 1

if dp[n] == 1:
    print("YES")
else:
    print("NO")