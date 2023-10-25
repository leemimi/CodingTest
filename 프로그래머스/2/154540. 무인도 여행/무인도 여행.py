from collections import deque
def solution(maps):
    answer = []
    n,m = len(maps), len(maps[0])
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    def bfs(x,y,start_num):
        cnt = start_num
        q = deque()
        visited[x][y] = True
        q.append((x,y))
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < n and 0<= ny<m and not visited[nx][ny]:
                    if maps[nx][ny] != 'X':
                        cnt += int(maps[nx][ny])
                        visited[nx][ny] = True
                        q.append((nx,ny))
        return cnt
    
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j]=True
                answer.append(bfs(i,j,int(maps[i][j])))
                
                                                        
    if len(answer)<1:
        answer.append(-1)
    else:
        answer.sort()
    return answer