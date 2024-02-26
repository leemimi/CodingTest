n = int(input())
k = int(input()) #사과개수
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    x,y = map(int, input().split())
    arr[x][y] = 1
L = int(input())
info = []
for _ in range(L):
    X,C = map(str, input().split())
    info.append((int(X),C))

#동 남 서 북 (오른쪽 머리)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(dir, c):
    if c == 'L':
        dir = (dir -1)%4
    else:
        dir = (dir+1)%4
    return dir


def simulate():
    x,y = 1,1
    dir = 0
    arr[x][y] = 2 #뱀의 머리가 있는곳
    time = 0
    idx = 0 #회전정보
    q = [(x,y)] #뱀의 몸통이 차지하고 있는 위치 정보(꼬리가 앞)
    while True:
        nx = x+ dx[dir]
        ny = y + dy[dir]
        # 맵안, 뱀위 몸통이 없는곳
        if 1<=nx and nx <=n and 1<=ny and ny<=n and arr[nx][ny]!=2:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)
                arr[px][py] = 0
            if arr[nx][ny] == 1:
                arr[nx][ny] = 2
                q.append((nx,ny))
        else:
            time +=1
            break
        x,y = nx,ny
        time +=1
        if idx < L and time == info[idx][0]:
            dir = turn(dir, info[idx][1])
            idx += 1
    return time


print(simulate())
