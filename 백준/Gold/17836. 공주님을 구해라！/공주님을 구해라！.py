import sys
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]
n,m,t = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]
def bfs(x,y):
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    q = deque()
    q.append((x,y))
    gramTime = 0
    while q:
        x,y = q.popleft()

        if (x, y) == (n - 1, m - 1):
            if gramTime:
                return min(visited[x][y], gramTime)
            return visited[x][y]

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if not (0<=nx<n and 0<=ny<m ):
                continue
            if arr[nx][ny] == 1 or visited[nx][ny] >-1:
                continue
            visited[nx][ny] = visited[x][y]+1
            q.append((nx,ny))
            if arr[nx][ny] == 2:
                gramTime = visited[nx][ny] + (abs(n-1-nx)+ abs(m-1-ny))

    if gramTime:
        return gramTime
    return t+1

res = bfs(0,0)
if res <= t:
    print(res)
else:
    print("Fail")
