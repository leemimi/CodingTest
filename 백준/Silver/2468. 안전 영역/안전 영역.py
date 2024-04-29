import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y, num,visited):
    q = deque()
    q.append((x,y,num))

    visited[x][y] = True

    while q:
        x,y,rain = q.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n :
                if not visited[nx][ny] and arr[nx][ny] > rain:
                    visited[nx][ny] = True
                    q.append((nx,ny, rain))



min_num = 101
max_num = -1
for i in range(n):
    for a in arr[i]:
        min_num = min(a, min_num)
        max_num = max(a, max_num)

res = -1
for k in range(max_num):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visited[i][j]:
                bfs(i,j,k,visited)
                cnt+=1
    res = max(cnt, res)

print(res)