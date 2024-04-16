n = int(input())
m = int(input())
vip = []
dp = [0]*(41)
for _ in range(m):
    a = int(input())
    vip.append(a)

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4,n+1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
if m>0:
    pre = 0
    for j in range(m):
        ans *= dp[vip[j] -1 -pre]
        pre = vip[j]
    ans *= dp[n-pre]
else:
    ans = dp[n]

print(ans)