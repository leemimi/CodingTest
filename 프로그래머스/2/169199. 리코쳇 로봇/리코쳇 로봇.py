from collections import deque
def solution(board):
    dx,dy = [0,0,-1,1], [1,-1,0,0]
    answer = 0
    goal_x, goal_y = 0,0
    n,m = len(board), len(board[0])
    visited = [[0]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                visited[i][j] = 1
                q.append((i,j))
                break
    def bfs():
        
        while q:
            px,py = q.popleft()
            if board[px][py] == 'G':
                return visited[px][py]
            for i in range(4):
                nx,ny = px,py
                while True:
                    nx,ny = nx+dx[i],ny+dy[i]
                    if 0<=nx<n and 0<=ny<m and board[nx][ny]=='D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx<0 or nx>=n or ny<0 or ny>=m:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[px][py] + 1
                    q.append((nx,ny))
        return -1
    answer = bfs()
    if answer >0:
        answer -=1
    return answer