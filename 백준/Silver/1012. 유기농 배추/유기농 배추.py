import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))


t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    res = 0
    arr = [[0]*m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for _ in range(k):
        a,b = map(int, input().split())
        arr[b][a] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                bfs(i,j)
                res +=1
    print(res)