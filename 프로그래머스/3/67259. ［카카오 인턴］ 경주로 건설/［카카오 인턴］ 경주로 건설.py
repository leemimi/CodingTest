import heapq
def solution(board):
    answer = 0
    q = []
    n = len(board)
    dist = [[[float('inf')]*4 for _ in range(n)] for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for d in range(4):
        dist[0][0][d] = 0
        
        heapq.heappush(q,(0,0,0,d)) #처음이 비용
        while q:
            cost, x,y, dir = heapq.heappop(q)
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                    new_cost = cost + 100 if dir == i else cost+ 600
                    if dist[nx][ny][i] > new_cost:
                        dist[nx][ny][i] = new_cost
                        heapq.heappush(q,(new_cost, nx,ny,i))
                        
            
    return min(dist[n-1][n-1])