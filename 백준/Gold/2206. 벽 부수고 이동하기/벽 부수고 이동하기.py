import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def bfs(a,b):
    q = deque()

    q.append((a,b,0))
    visited[a][b][0] = 1

    while q:
        x,y,b = q.popleft()

        if (x,y) == (n-1,m-1):
            return visited[x][y][b]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m :
                if arr[nx][ny] == 1 and b==0 and not visited[nx][ny][1]:
                    q.append((nx,ny,1))
                    visited[nx][ny][1] = visited[x][y][0] +1
                elif arr[nx][ny] == 0 and not visited[nx][ny][b]:
                    q.append((nx,ny,b))
                    visited[nx][ny][b] = visited[x][y][b]+1
    return 0

visited = [[[0]*2 for _ in range(m)]for _ in range(n)]
res = bfs(0,0)
if res:
    print(res)
else:
    print(-1)