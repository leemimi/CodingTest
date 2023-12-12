from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]


def bfs(a,b):

    q.append((a,b))
    visited[a][b] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx<n and 0<=ny<n and visited[nx][ny] != True and arr[nx][ny] == arr[x][y]:
                visited[nx][ny] = True
                q.append((nx,ny))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited = [[False]*n for _ in range(n)]
cnt = 0
q = deque()
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt+=1
visited = [[False]*n for _ in range(n)]
cnt1=0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1+=1

print(cnt, cnt1)