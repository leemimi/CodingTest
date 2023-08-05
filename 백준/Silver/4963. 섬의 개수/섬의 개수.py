from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,1,-1,1,-1]
def bfs(x,y):
    arr[x][y] = 0
    queue = deque([(x,y)])

    while queue:
        x,y = queue.popleft()

        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<h and 0<=ny<w:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    queue.append((nx,ny))



while True:
    w, h = map(int, input().split())
    if w == 0 and h==0 :
        break
    arr = []
    ans = 0
    visited = []

    for _ in range(h):
        arr.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i,j)
                ans +=1
    print(ans)