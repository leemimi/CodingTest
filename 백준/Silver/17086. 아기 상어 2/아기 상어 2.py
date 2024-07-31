import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

dx = [0,0,-1,1,-1,1,1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
q = deque()
def bfs():
    while q:
        x,y=  q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 0:
                    q.append((nx,ny))
                    arr[nx][ny] = arr[x][y]+1
    return
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))
ans = 0
bfs()
for i in range(n):
    for j in range(m):
        ans = max(ans, arr[i][j])

print(ans-1)