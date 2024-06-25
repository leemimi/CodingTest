import sys
input = sys.stdin.readline
from itertools import combinations
n,m = map(int, input().split())
t = []
target = 0
for _ in range(n):
    name, song = map(str, input().split())
    r=0
    for i in range(len(song)):
        if song[i] == 'Y':
            r |= (1 << i)
    target |= r
    if r:
        t.append(r)
ans =0
for i in range(1, n+1):
    for j in list(combinations(t,i)):
        base = 0
        for k in j:
            base |= k
        if target == base:
            ans = len(j)
            break
    if ans:
        break
print(ans if ans else -1)