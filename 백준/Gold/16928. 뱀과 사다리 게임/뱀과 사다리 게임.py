import sys
input = sys.stdin.readline
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

arr = [False]*101
arr[1] = True
cnt = 0
q = deque([1])


flag = True
while flag:

    for _ in range(len(q)):
        now = q.popleft()
        if now >=100:
            print(cnt)
            flag = False
            break

        for i in range(1,7):
            nx = now + i
            if nx<= 100 and not arr[nx]:
                arr[nx] = True
                if nx in ladders.keys() :
                    arr[ladders[nx]] = True
                    q.append((ladders[nx]))

                elif nx in snakes.keys():
                    arr[snakes[nx]] = True
                    q.append((snakes[nx]))
                else:
                    q.append(nx)
    cnt+=1