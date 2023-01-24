import sys
import heapq as hq

a=[]
n = int(input())
for i in range(n):
    x = int(sys.stdin.readline())
    if x==0:
        if len(a) == 0:
            print(0)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a,x)