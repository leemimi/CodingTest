import sys
input = sys.stdin.readline

import heapq
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

heapq.heapify(arr)
ans = 0
while len(arr)>1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    h = a+b
    ans += h
    if len(arr) <=0:
        break
    heapq.heappush(arr, h)

print(ans)