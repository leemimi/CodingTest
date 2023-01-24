import sys
import heapq as hq

abs_h=[]
n = int(input())
for i in range(n):
    x = int(sys.stdin.readline())
    if x==0:
        if len(abs_h) == 0:
            print(0)
        else:
            print(hq.heappop(abs_h)[1])
    else:
        hq.heappush(abs_h,(abs(x),x))