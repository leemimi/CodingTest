import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]
r,c =map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(r)]

visited = [[0]*c for _ in range(r)]
def bfs():

    while q:
        x,y = q.popleft()
        if (x,y) == (ax,ay):
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c :
                if (arr[nx][ny] =='.' or arr[nx][ny] == 'D') and arr[x][y] == 'S':
                    arr[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
                elif (arr[nx][ny] == '.' or arr[nx][ny] == 'S') and arr[x][y] == '*':
                    arr[nx][ny] = '*'
                    q.append((nx,ny))
    return "KAKTUS"



q = deque()
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            q.append((i,j))
        elif arr[i][j] == 'D':
            ax,ay = i,j
for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            q.append((i,j))
res = bfs()
print(res)