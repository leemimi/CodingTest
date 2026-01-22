import sys
input = sys.stdin.readline
import heapq

n = int(input())
d = int(input())
arr = []
for i in range(1,n):
    a = int(input())
    arr.append(-a)

heapq.heapify(arr)
cnt = 0
while arr:
    tmp = heapq.heappop(arr)
    tmp = -tmp
    if tmp >= d :
        cnt += 1
        d += 1
        tmp -=1
        heapq.heappush(arr, -tmp)
    else:
        break
print(cnt)