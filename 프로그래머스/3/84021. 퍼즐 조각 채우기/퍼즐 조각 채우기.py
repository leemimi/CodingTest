from collections import deque
def solution(game_board, table):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    answer = 0
    n = len(table)
    
    def bfs(x,y):
        visited[x][y] = True
        q=deque()
        q.append((x,y))
        vset= set()
        vset.add((x,y))
        
        while q:
            ci,cj = q.popleft()
            
            for i in range(4):
                nx = ci+dx[i]
                ny = cj+dy[i]
                
                if 0<=nx<n and 0<=ny<n and table[nx][ny]==1:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        vset.add((nx,ny))
        return vset
    
    def bfs1(x,y):
        visited[x][y] = True
        q=deque()
        q.append((x,y))
        vset= set()
        vset.add((x,y))
        
        while q:
            ci,cj = q.popleft()
            
            for i in range(4):
                nx = ci+dx[i]
                ny = cj+dy[i]
                
                if 0<=nx<n and 0<=ny<n and game_board[nx][ny]==0:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        vset.add((nx,ny))
        return vset
    
    
    visited = [[0]*len(table[0]) for _ in range(len(table))]
    blocks = []
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1 and not visited[i][j]:
                blocks.append(bfs(i,j))
    boards = []            
    visited = [[0]*len(game_board[0]) for _ in range(len(game_board))]            
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == 0 and not visited[i][j]:
                boards.append(bfs1(i,j))
    
    #좌표 표준으로 만들기
    used = [False] * len(blocks)
    def normalize(arr):
        min_x = min(x for x,y in arr)
        min_y = min(y for x,y in arr)
        return sorted([(x-min_x,y-min_y)for x,y in arr])
    def rotate(arr):
        return [(y,-x) for x,y in arr]
    #빈칸에 넣기
    for board in boards:
        b = normalize(board)
        flag = False
        for idx, block in enumerate(blocks):
            if used[idx] :
                continue
            tmp = block
            for _ in range(4):
                tmp = rotate(tmp)
                if normalize(tmp) == b:
                    used[idx] = True
                    answer += len(tmp)
                    flag = True
                    break
            if flag:
                break
    return answer