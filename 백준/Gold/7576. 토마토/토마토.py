import sys
from collections import deque
m,n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
days =0
queue=deque([])
def bfs():

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+ dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0:
                    arr[nx][ny] = arr[x][y]+1
                    queue.append((nx,ny))

result=0
for i in range(n):
    for j in range(m):
        if(arr[i][j]==1):
            queue.append([i,j])
bfs()

for row in arr:
    for num in row:
        if(num==0):
            print(-1)
            exit(0)
    result = max(result,max(row))

print(result-1)