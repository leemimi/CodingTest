import sys
from itertools import combinations
INF = 1e9

n,m = map(int, input().split())
arr =[[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i==j:
            arr[i][j] = 0

#1시간에 양방향으로 갈 수 있음
for _ in range(m):
    a,b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            arr[a][b] = min(arr[a][b], arr[a][k]+arr[k][b])

city = [i for i in range(1,n+1)]
chicken = list(combinations(city,2))

ans = (1e9, 1,2)
for ch in chicken:
    a,b = ch
    tmp = 0
    for c in city:
        tmp += min(arr[c][a], arr[c][b])
    if ans[0]>tmp:
        ans = (tmp, a,b)

print(ans[1], ans[2], ans[0]*2)
