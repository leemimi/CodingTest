import sys
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

time = 1
def bfs():
    global melt
    melt = deque([])
    q = deque([(0,0)])

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+ dx[i]
            ny = y +dy[i]

            if 0<= nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if arr[nx][ny] == 0 :
                    q.append((nx,ny))
                elif arr[nx][ny] == 1:
                    melt.append((nx,ny))
    for x,y in melt:
        arr[x][y] = 0
    return len(melt)


cheese = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cheese += 1

while True:
    visited = [[0] * m for _ in range(n)]
    cnt = bfs()

    cheese -= cnt
    if cheese == 0:
        print(time)
        print(cnt)
        break
    time +=1
