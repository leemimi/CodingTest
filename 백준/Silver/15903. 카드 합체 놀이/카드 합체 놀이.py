import sys
input = sys.stdin.readline
import heapq

n,m = map(int, input().split())
arr = list(map(int, input().split()))

heapq.heapify(arr)
for i in range(m):
    if len(arr)>1:
        x = heapq.heappop(arr)
        y = heapq.heappop(arr)

        b = x+y
        x=b
        y=b
        heapq.heappush(arr, x)
        heapq.heappush(arr, y)
print(sum(arr))