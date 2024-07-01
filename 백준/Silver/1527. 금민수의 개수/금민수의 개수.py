import sys
input = sys.stdin.readline
from itertools import product
a,b =map(int, input().split())

x = len(str(a))
y = len(str(b))
cnt = 0
for i in range(x,y+1):
    arr = list(product([4,7], repeat= i))
    for num in arr:
        n = int(''.join(map(str, num)))
        if a<=n<=b:
            cnt+=1

print(cnt)