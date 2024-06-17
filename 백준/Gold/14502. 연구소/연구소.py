import copy
import math
import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def bfs():
    q = deque()
    land = copy.deepcopy(arr)

    for i in range(n):
        for j in range(m):
            if land[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if land[nx][ny] == 0:
                    land[nx][ny] = 2
                    q.append((nx,ny))
    global ans
    cnt = 0
    for i in range(n):
        cnt += land[i].count(0)
    ans = max(ans, cnt)



def makeWall(k):
    if k == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makeWall(k+1)
                arr[i][j] = 0
ans = 0
makeWall(0)
print(ans)