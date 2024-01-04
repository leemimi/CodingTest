import sys
input = sys.stdin.readline
from collections import deque
n,m,k = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def bfs(a,b,z):
    q = deque()
    q.append((a,b,z))

    while q:
        x,y,b = q.popleft()

        if (x,y) == (n-1,m-1):
            return visited[x][y][b]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if 0<=nx<n and 0<=ny<m :
                if arr[nx][ny] == 1 and b>0 and not visited[nx][ny][b-1]:
                    q.append((nx,ny,b-1))
                    visited[nx][ny][b-1] = visited[x][y][b] +1
                elif arr[nx][ny] == 0 and not visited[nx][ny][b]:
                    q.append((nx,ny,b))
                    visited[nx][ny][b] = visited[x][y][b]+1
    return -1

visited = [[[0]*(k+1) for _ in range(m)]for _ in range(n)]
visited[0][0][k] = 1
res = bfs(0,0,k)
print(res)