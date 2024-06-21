import sys
input = sys.stdin.readline
import heapq

q = []
x = int(input())
for _ in range(x):
    a,b = map(int, input().split())
    heapq.heappush(q, (a,b))

q.sort()
pc = [0 for i in range(x)]
cnt = [0 for i in range(x)]

while q:
    st,end = heapq.heappop(q)
    for i in range(len(pc)):
        if pc[i] <= st:
            pc[i] = end
            cnt[i] +=1
            break
idx = len(pc) - cnt.count(0)
print(idx)
print(*cnt[:idx])