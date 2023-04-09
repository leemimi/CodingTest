from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt =0
global area

queue = deque([])
def bfs(x,y,arr,visited,area):
    queue.append([x,y])
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()
        area+=1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == True or arr[nx][ny] == 0:
                continue
            visited[nx][ny] = 1
            queue.append((nx, ny))
    return area

a=[]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt +=1
            a.append(bfs(i,j,arr,visited,0))

print(cnt)
a.sort()
for i in a:
    print(i)