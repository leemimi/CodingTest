import sys
input = sys.stdin.readline

r,c,t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

def spread():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if arr[i][j] != -1 and arr[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i +dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1 :
                        visited[nx][ny] += arr[i][j]//5
                        cnt += arr[i][j]//5
                arr[i][j] -= cnt

    for i in range(r):
        for j in range(c):
            arr[i][j] += visited[i][j]

def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    dir = 0
    before = 0
    x,y = up,1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x==up and y==0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir+=1
            continue
        arr[x][y], before = before, arr[x][y]
        x =nx
        y =ny

def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

#공기청정기 위치 찾기
up =-1
down = -1
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i+1
        break

for _ in range(t):
    spread()
    air_up()
    air_down()


answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] >0 :
            answer+=arr[i][j]
print(answer)