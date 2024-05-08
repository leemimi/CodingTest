import sys
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def bfs(x,y):
    global cnt
    q = deque()
    visited[x][y] = 1

    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = 1
                    arr[nx][ny] = cnt
                    q.append((nx,ny))

def bridge(v):
    q = deque()

    dist = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == v:
                dist[i][j] = 0
                q.append((i,j))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if 0<=nx<n and 0<=ny<n :
                if arr[nx][ny] > 0 and arr[nx][ny] != v:
                    return dist[x][y]
                elif arr[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))
    return int(1e9)


cnt = 1
res = int(1e9)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            arr[i][j] = cnt
            bfs(i,j)
            cnt+=1
for v in range(1,n):
    res = min(res, bridge(v))


print(res)