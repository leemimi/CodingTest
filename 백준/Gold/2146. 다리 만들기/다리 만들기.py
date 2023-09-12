import sys
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def find_bridge(k):
    q = deque()

    dist = [[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == k:
                dist[i][j] = 0
                q.append((i,j))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<=ny < n:
                if arr[nx][ny] > 0 and arr[nx][ny] !=v:
                    return dist[x][y]
                elif arr[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] +1
                    q.append((nx,ny))
    return int(1e9)


def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] :
                if arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    arr[nx][ny] = num
                    q.append((nx,ny))


n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
visited =[[False]*n for _ in range(n)]
ground = []

num = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j] :
            visited[i][j] = True
            arr[i][j] = num
            bfs(i,j)
            num+=1
res = sys.maxsize
for v in range(1, n):
    res = min(res, find_bridge(v))
print(res)