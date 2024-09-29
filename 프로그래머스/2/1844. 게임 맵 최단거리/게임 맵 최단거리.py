from collections import deque
def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    q = deque()
    answer = 0
    
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    vistied = [[0]*m for _ in range(n)]
    vistied[0][0] = 1
    q.append((0,0))

    
    while q:
        
        x,y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<n and 0<=ny<m and not vistied[nx][ny]:
                if maps[nx][ny] == 1:
                    vistied[nx][ny] = vistied[x][y] +1
                    q.append((nx,ny))
    
    if vistied[n-1][m-1] == 0:
        return -1
    
    return vistied[n-1][m-1]