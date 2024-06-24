import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
from itertools import permutations
n = int(input())
arrs = list(map(int, input().split()))
ans = 0
def dfs(arr):
    sums = 0

    for i in range(n-1):
        sums += abs(arr[i+1]-arr[i])
    return sums

prr = list(permutations(arrs,n))
for p in prr:
    ans = max(ans, dfs(p))

print(ans)