import sys
from collections import deque
input = sys.stdin.readline
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    visited = [False]*10000
    q = deque()
    q.append((a,""))

    while q:
        num, path = q.popleft()
        visited[num] = True
        if num == b:
            print(path)
            break

        d = (2*num)%10000
        if not visited[d]:
            q.append((d, path+'D'))
            visited[d] = True
        s = (num-1)%10000
        if not visited[s]:
            q.append((s, path+'S'))
            visited[s] = True


        l = (num//1000) + (num%1000)*10
        if not visited[l]:
            q.append((l, path+'L'))
            visited[l] = True

        r = (num//10) + (num%10)*1000
        if not visited[r]:
            q.append((r, path+'R'))
            visited[r] = True