n,m = map(int, input().split())
r,c,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[0]*m for _ in range(n)]
visited[r][c] = 1
cnt = 1
while True:
    flag = 0
    for i in range(4):
        d = (d+3)%4
        nr = r + dx[d]
        nc = c+dy[d]

        if 0<=nr<n and 0<=nc<m and arr[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt+=1
                r = nr
                c = nc
                flag = 1
                break
    if flag == 0:
        if arr[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dx[d], c-dy[d]