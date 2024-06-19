import sys
from collections import deque

n,m = map(int, input().split())
ladders = {}
for _ in range(n):
    a,b = map(int, input().split())
    ladders[a] = b
snakes = {}
for _ in range(m):
    a,b = map(int, input().split())
    snakes[a] = b

q = deque([1])
visited = [False]*101
visited[1] = False
cnt = 0
flag = True
while flag:

    for _ in range(len(q)):
        now = q.popleft()

        if now == 100:
            print(cnt)
            flag =False
            break
        for d in range(1,7):
            nx = now+ d
            if nx <= 100 and not visited[nx]:
                visited[nx]=True

                if nx in ladders.keys():
                    visited[ladders[nx]]=True
                    q.append(ladders[nx])
                elif nx in snakes.keys():
                    visited[snakes[nx]]=True
                    q.append(snakes[nx])
                else:
                    q.append(nx)
    cnt+=1