from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
time = 0

q =deque()
def airCheeze(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy +dy[i]

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and arr[nx][ny] ==0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                elif arr[nx][ny] == 1:
                    visited[nx][ny] = visited[nx][ny] +1

while True:
    visited = [[0]*m for _ in range(n)]

    airCheeze(0, 0)
    time +=1
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                arr[i][j] = 0


    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt+=1
    if cnt == n*m:
        break

print(time)