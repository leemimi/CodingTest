import math
import sys
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n,l,r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

day = 0

def bfs(i,j):
    q = deque()
    q.append((i,j))

    visited[i][j] = True
    qq = [(i,j)]
    sum = arr[i][j]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if l<=abs(arr[nx][ny] - arr[x][y])<=r:
                    visited[nx][ny] = True
                    qq.append((nx,ny))
                    sum += arr[nx][ny]
                    q.append((nx,ny))
    for x,y in qq:
        arr[x][y] = math.floor(sum/len(qq))
    return len(qq)



while True:
    visited = [[False]*n for _ in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j] :
                if bfs(i,j)>1:
                    check = True
    if not check:
        break
    day+=1

print(day)