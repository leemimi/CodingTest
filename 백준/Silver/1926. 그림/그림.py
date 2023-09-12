from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    global psize, arr, visited
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
                if arr[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    count +=1
    return count


n,m = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]
cnt = 0
psize = 0

visited =[[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0 :
            cnt+=1
            psize = max(bfs(i,j),psize)

print(cnt)
print(psize)
