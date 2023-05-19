x = int(input())

dp= [0]*(x+1)
stairs = [0]*(x+1)
for i in range(1,x+1):
    stairs[i] = int(input())

if x == 1:
    print(stairs[x])
    exit()
elif x == 2:
    print(stairs[1]+stairs[2])
    exit()
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1]+stairs[2]
for i in range(3,x+1):
    dp[i] = max(dp[i-2]+stairs[i],dp[i-3]+stairs[i]+stairs[i-1])

print(dp[-1])