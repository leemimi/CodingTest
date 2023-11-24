from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def find_land(a,b,land):
    global visited, q, land_with,cnt
    visited[a][b] = True
    q.append((a,b))
    
    while q:
        x,y = q.popleft()
        cnt.add(y+1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx<len(land) and 0<= ny <len(land[0]) and not visited[nx][ny]:
                if land[nx][ny] == 1:
                    visited[nx][ny] = True
                    land_with+=1
                    
                    q.append((nx,ny))

def solution(land):
    
    global visited, q, land_with, cnt
    visited= [[False]*len(land[0]) for _ in range(len(land))]
    land_with = 0
    q = deque()
    
    dict = {}
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if not visited[i][j] and land[i][j] == 1:
                land_with = 1
                cnt = set()
                find_land(i,j,land)
                
                for c in cnt:
                    if c in dict:
                        dict[c] += land_with
                    else:
                        dict[c] = land_with
                    
    
    answer = dict.values()
    return max(answer)



                    