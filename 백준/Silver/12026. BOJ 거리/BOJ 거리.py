import sys
n = int(input())
arr = ['0']+list(map(str, input().rstrip()))
dp = [sys.maxsize]*(n+1)
dp[1] = 0
now ='B'
for i in range(1,n+1):
    for j in range(i):
        if arr[j] == 'B' and arr[i] != 'O':
            continue
        elif arr[j] == 'O' and arr[i] != 'J':
            continue
        elif arr[j] =='J' and arr[i] != 'B':
            continue
        dp[i] = min(dp[j]+pow(i-j,2), dp[i])

if dp[n] == sys.maxsize:
    print(-1)
else:
    print(dp[n])