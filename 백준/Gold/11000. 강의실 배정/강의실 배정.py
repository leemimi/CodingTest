import sys, heapq
input = sys.stdin.readline

n =int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
cnt = 0

arr.sort()
heap = []
heapq.heappush(heap, arr[0][1])

for i in range(1,n):
    if arr[i][0] < heap[0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap,arr[i][1])

print(len(heap))