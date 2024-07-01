import sys
input = sys.stdin.readline

from itertools import permutations


n = int(input())
arr = list(map(int, input().split()))

def dfs(r):
    sums = 0

    for i in range(n-1):
        sums+= abs(r[i] - r[i+1])
    return sums


li = list(permutations(arr, n))
ans = 0
for l in li:
    ans = max(ans, dfs(l))

print(ans)