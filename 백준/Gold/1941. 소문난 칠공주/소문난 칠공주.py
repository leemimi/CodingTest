import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
from collections import deque



dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(L,start):
    global ans
    if L == 7:
        if bfs():
            ans+=1
        return

    for i in range(start,25):
        visited[i//5][i%5] = 1
        dfs(L+1, i+1)
        visited[i//5][i%5] = 0

def bfs():
    so = 0
    do = 0
    xx,yy = 0,0
    find_arr = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                find_arr[i][j] = visited[i][j]
                xx = i
                yy = j

    q = deque()
    q.append((xx,yy))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<5 and 0<=ny<5:
                if find_arr[nx][ny]:
                    find_arr[nx][ny] = 0
                    q.append((nx,ny))
                    if arr[nx][ny] == 'S':
                        so+=1
                    else:
                        do +=1
                        if do>3:
                            return False
    if so + do !=7 :
        return False
    elif so < 4:
        return False
    else:
        return True


arr = [list(map(str, input().rstrip()))for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
ans = 0
dfs(0, 0)
print(ans)