import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
from collections import deque

R,C = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(R)]
start = (0,0)
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(now,visited, alp):
    global answer

    if len(alp) > answer:
        answer = len(alp)

    visited[now[0]][now[1]] = True
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0<=nx<R and 0<=ny<C:
            if arr[nx][ny] not in alp and not visited[nx][ny] :
                visited[nx][ny] = True
                dfs((nx,ny), visited, alp+arr[nx][ny])
                visited[nx][ny] = False




answer = 0
visited = [[False]*C for _ in range(R)]
visited[0][0] = True
dfs(start, visited, arr[0][0])
print(answer)