import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
import heapq


key = input().rstrip()

dp = [0]*len(key)
n = len(key)

if n == 1:
    print(0 if key[0] =='0' else 1)
    exit()

dp = [0]*n
dp[0] = 1

if key[0] == '0':
    print(0)
    exit()

if key[1] != '0':
    dp[1] += dp[0]

if 10 <= int(key[:2]) <= 26:
    dp[1] += 1

for i in range(2,len(key)):
    if key[i] != '0':
        dp[i] += dp[i-1]
    if 10 <= int(key[i-1:i+1])<=26:
        dp[i] += dp[i-2]

print(dp[-1]%1000000)