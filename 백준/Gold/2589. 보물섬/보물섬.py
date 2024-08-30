import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

r,c = map(int, input().split())
arr = [list(map(str, input().strip()))for _ in range(r)]


def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited = [[0]*c for _ in range(r)]
    visited[i][j] = 1
    cnt = 0
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if arr[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]+1
                    cnt = max(cnt, visited[nx][ny])
                    q.append((nx,ny))

    return cnt-1



ans = 0
q = deque()
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            if 0 <= i - 1 < r and 0 <= i + 1 < r:
                if arr[i-1][j] =='L' and arr[i+1][j] =='L':
                    continue
            if 0<= j-1<c and 0<= j+1<c:
                if arr[i][j-1] =='L' and arr[i][j+1] == 'L':
                    continue
            ans = max(ans, bfs(i,j))
print(ans)