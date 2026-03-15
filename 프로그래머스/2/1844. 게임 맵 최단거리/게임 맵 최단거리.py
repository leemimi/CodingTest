from collections import deque
def solution(maps):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    q.append((0,0))
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
    
        
        
    
    answer = 0
    return visited[n-1][m-1] if visited[n-1][m-1] > 1 else -1