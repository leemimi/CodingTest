from collections import deque

steps = [(-2,1),(-1,2),(1,2),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
def bfs(x,y,a,b):
    q = deque()
    q.append((x,y))
    arr[x][y] = 1
    while q:
        x,y = q.popleft()

        if x == a and y == b:
            return arr[x][y] - 1

        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if 0<=nx<l and 0<=ny<l and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y]+1
                q.append((nx,ny))


K = int(input())
for _ in range(K):
    l = int(input())
    x,y = map(int,input().split())
    a,b = map(int,input().split())

    if x == a and y ==b :
        print(0)
        continue
    arr = [[0]*l for _ in range(l)]
    print(bfs(x,y,a,b))
