import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for i in range(n):
    arr = list(map(int, input().split()))
    if not q:
        for num in arr:
            heapq.heappush(q, num)
    else:
        for num in arr:
            if q[0] < num:
                heapq.heappush(q, num)
                heapq.heappop(q)
print(q[0])