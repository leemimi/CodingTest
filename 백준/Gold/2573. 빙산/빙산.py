import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
q =deque()
def bfs(x,y):
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] : continue

                if arr[nx][ny] == 0 and arr[x][y] > 0:
                    arr[x][y] -=1
                elif arr[nx][ny] > 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    return 1

year =0
while True:
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j]:
                visited[i][j] = 1
                cnt+=bfs(i,j)
    if cnt>1:
        break
    if not any([j for i in arr for j in i]):
        year = 0
        break
    year+=1


print(year)