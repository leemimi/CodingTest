import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
moves = []
for i in range(m):
    temp = list(map(int,input().split()))
    moves.append([temp[0]-1,temp[1]])

clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

ddx = [1, 1, -1, -1]
ddy = [-1, 1, 1, -1]

for d,s in moves:
    ms = deque()
    new_clouds = []
    for x,y in clouds:
        nx = (x + dx[d] * s + n) % n
        ny = (y + dy[d] * s + n) % n

        arr[nx][ny]+=1
        new_clouds.append((nx,ny))
        ms.append((nx,ny))
    while ms:
        x,y = ms.popleft()
        cnt = 0
        for i in range(4):
            nx = x + ddx[i]
            ny = y +ddy[i]

            if 0<=nx<n and 0<=ny<n and arr[nx][ny] >0:
                cnt+=1
        arr[x][y] +=cnt

    clouds = []
    for i in range(n):
        for j in range(n):
            if (i,j) not in new_clouds:
                if arr[i][j] >=2:
                    clouds.append((i,j))
                    arr[i][j]-=2
ans = sum(map(sum, arr))
print(ans)