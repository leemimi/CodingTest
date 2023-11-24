
import sys
n= int(input())

def run(r,c,a,b):
    return abs(r-a)+abs(c-b)
check = []
for _ in range(n):
    x,y =map(int, input().split())
    check.append((x,y))

distence = [0]
for i in range(n-1):
    dist = run(check[i][0],check[i][1],check[i+1][0],check[i+1][1])
    distence.append(dist)
total = sum(distence)
res = sys.maxsize
dist = 0
for i in range(1,n-1):
    dist = total - (distence[i+1]+distence[i]) + run(check[i+1][0],check[i+1][1],check[i-1][0],check[i-1][1])
    res = min(res, dist)
print(res)