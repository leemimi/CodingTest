from collections import deque


def bfs(x,y):
    q = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1:
                arr[nx][ny] =0
                q.append((nx,ny))




T = int(input())
for _ in range(T):
    m,n,k = map(int,input().split())

    arr = [[0]*m for i in range(n)]

    for _ in range(k):
        i,j = map(int,input().split())
        arr[j][i] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] = 0
                bfs(i,j)
                cnt+=1

    print(cnt)


