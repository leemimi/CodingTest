from collections import deque
def solution(maps):

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    def bfs(start, end):
        visited = [[False]*m for _ in range(n)]
        q = deque([(start[0],start[1],0)])
        visited[start[0]][start[1]] = True
        
        while q:
            x,y,cnt = q.popleft()
            if (x,y) == end:
                return cnt
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] != 'X' and visited[nx][ny] != True:
                    visited[nx][ny] = True
                    q.append((nx,ny,cnt+1))
        return 0

    n = len(maps)
    m = len(maps[0])
    check = [(),(),()]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                check[0] = (i,j)
            elif maps[i][j] == "E":
                check[1] = (i,j)
            elif maps[i][j] == "L":   
                check[2] = (i,j)
                
    
    res1 = bfs(check[0],check[2])
    res2 = bfs(check[2],check[1])
    if res1 and res2:
        return res1+res2
    else:
        return -1