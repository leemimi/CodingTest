import sys

from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]
n,k = map(int, input().split())
arr = []
virus = []
for _ in range(n):
    c = list(map(int, input().split()))
    arr.append(c)
for i in range(n):
    for j in range(n):
        if arr[i][j] !=0:
            virus.append((arr[i][j],i,j,0))

s, bx,by = map(int, input().split())
virus.sort()
q = deque(virus)

while q:
    num ,x, y, time = q.popleft()
    if time == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if arr[nx][ny] == 0:
            arr[nx][ny] = num
            q.append((num,nx,ny,time+1))



print(arr[bx - 1][by - 1])