from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
H,W,Si,Sj,Fi,Fj = map(int, input().split())
Si,Sj,Fi,Fj = Si-1,Sj-1,Fi-1,Fj-1
dx = [0,0,1,-1]
dy = [1,-1,0,0]

walls = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            walls.append((i,j))


def check(x,y):
    for wi, wj in walls:
        if x <= wi < x + H and y <= wj < y + W:
           return False
    return True


def bfs(ci,cj):
    q = deque()
    q.append((ci,cj))
    visited[ci][cj] = 1
    while q:
        x, y = q.popleft()
        
        if (x,y) == (Fi,Fj):
            return visited[x][y] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and 0<=nx+H-1<n and 0<=ny+W-1<m:
                if check(nx,ny):
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    return -1
    


visited = [[0]*m for _ in range(n)]
print(bfs(Si,Sj))