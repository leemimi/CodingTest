n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

boomerangs = [
    [(0,0), (0,-1),(1,0)],
    [(0, 0), (0, -1), (-1, 0)], # 위 + 왼쪽
    [(0, 0), (-1, 0), (0, 1)],  # 위 + 오른쪽
    [(0, 0), (0, 1), (1, 0)]
]
visited = [[False]*m for _ in range(n)]
answer = 0

def dfs(L, cnt):
    global answer
    if L == n*m :
        answer = max(answer, cnt)
        return
    
    x = L//m
    y = L%m
    if not visited[x][y]:
        for boo in boomerangs:
            flag = True
            points = []
            for dx, dy in boo:
                nx = x+dx
                ny = y+dy
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    points.append((nx,ny))
                else:
                    flag = False
                    break
            if flag:
                for px,py in points:
                    visited[px][py] = True
                    
                v = a[x][y]*2 + sum(a[px][py] for px,py in points if (px,py)!= (x,y))
                dfs(L+1, cnt+v)
                for px,py in points:
                    visited[px][py] = False
    dfs(L+1, cnt)
                        

dfs(0,0)
print(answer)