from collections import deque


def bfs(x,y,maps,visited,n,m):
    q = deque()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q.append([x,y])
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                if visited[nx][ny]==0:
                    visited[nx][ny] =1
                    maps[nx][ny] = maps[x][y]+1
                    q.append([nx,ny])
                
    if maps[n-1][m-1] == 1:
        return -1
    return maps[n-1][m-1]
    
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited=[[0]*m for _ in range(n)]
    visited[0][0] = 1
    
    return bfs(0,0,maps,visited,n,m)