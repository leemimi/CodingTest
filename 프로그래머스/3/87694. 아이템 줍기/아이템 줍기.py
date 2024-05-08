from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    answer = 0 
    arr = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x:x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    arr[i][j] = 0
                elif arr[i][j] != 0:
                    arr[i][j] = 1
                    
    cx, cy, ix, iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY

    q = deque()
    q.append((cx,cy))
    
    while q:
        x,y = q.popleft()

        if x == ix and y == iy:
            answer = visited[x][y]//2
            break

        for i in range(4):
            nx = x+ dx[i]
            ny = y + dy[i]

            if arr[nx][ny] ==1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                q.append((nx,ny))
                
                
    return answer