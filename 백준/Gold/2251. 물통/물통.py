import sys
from collections import deque
input = sys.stdin.readline

A,B,C = map(int, input().split())
q =deque()
res = []
q.append((0,0,C))
visited = [[0] * 201 for i in range(201)]
def bfs():
    while q:
        a,b,c = q.popleft()
        if visited[a][b] ==1:
            continue
        visited[a][b] = 1

        if a == 0:
            res.append(c)

        if a+b > B:
            q.append((a+b-B,B,c))
        else:
            q.append((0,a+b,c))

        if a+c >C:
            q.append((a+c-C,b,C))
        else:
            q.append((0,b,a+c))

        if b+c > C:
            q.append((a,b+c-C,C))
        else:
            q.append((a,0,b+c))

        if a+b >A:
            q.append((A, a+b-A, c))
        else:
            q.append((a+b,0,c))

        if c+a > A:
            q.append((A,b,c+a-A))
        else:
            q.append((a+c,b,0))

        if c+b > B:
            q.append((a,B,c+b-B))
        else:
            q.append((a,b+c, 0))
bfs()
res = list(res)
res.sort()
print(*res)