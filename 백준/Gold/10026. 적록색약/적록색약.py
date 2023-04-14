from collections import deque

def bfs(x,y):
    queue.append((x,y))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[x][y] =True
    while queue:

        x,y =queue.popleft()
        for i in range(4):
            nx = dx[i] +x
            ny = dy[i] +y
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                visited[nx][ny] =True
                queue.append((nx,ny))


n = int(input())
arr = [list(map(str, input())) for _ in range(n)]


cnt1=0
cnt2=0
queue = deque()
visited = [[False] * n for _ in range(n)]
#적록색약이 아닐때!
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            cnt1 +=1
            bfs(i,j)
#적록색약일때 !
for i in range(n):
    for j in range(n):
        if arr[i][j] =='G':
            arr[i][j]='R'

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            cnt2 +=1
            bfs(i,j)

print(cnt1, cnt2)
