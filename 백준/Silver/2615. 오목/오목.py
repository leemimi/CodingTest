import sys
input = sys.stdin.readline

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
arr = [list(map(int, input().split())) for _ in range(19)]

def bfs(x,y,om):
    for i in range(4):
        nx, ny = x + dx[i], y+dy[i]
        cnt = 1

        while 0<=nx<19 and 0<=ny<19 and arr[nx][ny] == om:
            cnt +=1

            if cnt == 5:
                if 0 <= x-dx[i]<19 and 0<=y-dy[i]<19 and arr[x-dx[i]][y-dy[i]] == om:
                    break
                if 0 <= nx+dx[i]<19 and 0<=ny+dy[i]<19 and arr[nx+dx[i]][ny+dy[i]] == om:
                    break
                print(om)
                print(x+1, y+1)
                exit(0)
            nx += dx[i]
            ny += dy[i]


for i in range(19):
    for j in range(19):
        if arr[i][j] == 1 or arr[i][j] == 2:
            om = arr[i][j]
            bfs(i,j,om)
print(0)