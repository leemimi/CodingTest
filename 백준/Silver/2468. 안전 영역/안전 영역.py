from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,value, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1


    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))


n = int(input())
arr = []
max_num = 0
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] > max_num:
            max_num = arr[i][j]



result = 0
for k in range(max_num):
    visited = [[0] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and visited[i][j] == 0:
                bfs(i,j,k,visited)
                ans+=1
    result = max(result, ans)

print(result)
