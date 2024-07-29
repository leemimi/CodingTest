import sys
input = sys.stdin.readline
from collections import deque

r,c =map(int, input().split())
arr = [ list(map(str, input().rstrip())) for _ in range(r)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def run():
    global flag
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if (0 <= nx < r and 0 <= ny < c):
                if arr[nx][ny] == '.':
                    cnt += 1
            else:
                cnt+=1
                continue
        if cnt >= 3:
            flag.append((x, y))

q= deque()
for i in range(r):
    for j in range(c):
        if arr[i][j] =='X':
            q.append((i,j))
flag = []
run()

for i,j in flag:
    arr[i][j] = '.'

x1 =0
y1 = c-1
x2 = 0
y2 = 0
for i in range(0,r):
    if 'X' in arr[i]:
        x1 = i
        break
for i in range(r-1,-1,-1):
    if 'X' in arr[i]:
        x2 = i
        break

for i in range(x1, x2+1):
    for j in range(c):
        if arr[i][j] == 'X':
            y1 = min(y1, j)
            y2 = max(y2, j)

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        print(arr[i][j], end='')
    print()