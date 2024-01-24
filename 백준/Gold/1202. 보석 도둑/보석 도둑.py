import heapq
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
dia = []
for _ in range(n):
    a,b = map(int,input().split())
    dia.append((a,b))
bags = []
for _ in range(k):
    j = int(input())
    bags.append(j)
bags.sort()
dia.sort()
res = 0

tmp = []

for b in bags:
    while dia and dia[0][0] <= b:
        heapq.heappush(tmp, -dia[0][1])
        heapq.heappop(dia)

    if tmp:
        res -= heapq.heappop(tmp)
print(res)