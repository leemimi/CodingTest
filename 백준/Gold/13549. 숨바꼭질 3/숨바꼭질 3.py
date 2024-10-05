import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int,input().split())
ans = 0
q = deque()
visited=[False]*100001
q.append([N,0])

while True:
    x,cnt = q.popleft()

    if x == K:
        ans = cnt
        break

    if x>=0 and x<100001:
        if not visited[x]:
            q.append([x*2, cnt])
            q.append([x-1,cnt+1])
            q.append([x+1,cnt+1])
            visited[x] = True


print(ans)