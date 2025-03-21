from collections import deque
def solution(storage, requests):
    answer = 0
    n = len(storage)
    m = len(storage[0])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    storage = [list(row) for row in storage]
    
    
    def is_out(storage, num, i,j):
        visited = [[False] * m for _ in range(n)]
        q = deque()
        q.append((i, j))
        visited[i][j] = True
        
        while q:
            x,y = q.popleft()
            if x==0 or y==0 or x==n-1 or y==m-1:
                return True
            for k in range(4):
                nx = x+ dx[k]
                ny = y + dy[k]
                if 0<= nx< n and 0<=ny<m and not visited[nx][ny]:
                    if storage[nx][ny] == '.':
                        visited[nx][ny] = True
                        q.append((nx,ny))
        return False
        
    
    #두개 꺼내기
    def crane(storage, num):
        for i in range(n):
            for j in range(m):
                if storage[i][j] == num:
                    storage[i][j] = '.'
                
    #외부 물류 꺼내기
    #1.배열에서 해당 번호의 값을 찾음 -> 그 번호가 외부와 연결되어있는지 확인
    def fork(storage,num):
        access = []
        for i in range(n):
            for j in range(m):
                if storage[i][j] == num:
                    if is_out(storage, num, i,j):
                        access.append((i,j))
        for a,b in access:
            storage[a][b] = '.'
            
            
        
    for req in requests:
        if len(req) == 1:
            fork(storage, req[0])
        else:
            crane(storage, req[0])
    #계산
    for i in range(n):
        for j in range(m):
            if storage[i][j] != '.':
                answer+=1
    
    return answer