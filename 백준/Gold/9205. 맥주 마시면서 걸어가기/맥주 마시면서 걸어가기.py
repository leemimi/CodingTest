from collections import deque
def bfs():
    global mac, fes, cnt
    q = deque()
    q.append((hx,hy))

    while q:
        x,y = q.popleft()
        if abs(x-fx) + abs(y-fy) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx,ny = arr[i]
                if abs(nx-x) + abs(ny-y) <= 1000:
                    visited[i]  = 1
                    q.append((nx,ny))
    print('sad')
    return


t = int(input())
for _ in range(t):
    mac = 20
    cnt = 0
    n = int(input())
    hx,hy = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    fx,fy = map(int,input().split())
    visited = [0 for _ in range(n + 1)]
    bfs()