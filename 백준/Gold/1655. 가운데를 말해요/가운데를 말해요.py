import sys
input = sys.stdin.readline
import heapq

n = int(input())
mah = []
mih = []

for i in range(n):
    num = int(input())
    if len(mah) == len(mih):
        heapq.heappush(mah,-num)
    else:
        heapq.heappush(mih,num)
    if len(mah)>=1 and len(mih) >=1 and mah[0]*-1 > mih[0]:
        max_value = heapq.heappop(mah)*-1
        min_value = heapq.heappop(mih)
        heapq.heappush(mah, min_value * -1)
        heapq.heappush(mih, max_value)

    print(mah[0]*-1)