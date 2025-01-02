import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
def bfs(x,y):
    global cnt
    q= deque()
    q.append((x,y,0))
    visited[x][y][0] = 1

    while q:
        sx, sy, break_cnt = q.popleft()

        if (sx, sy) == (n-1, m-1):
            return visited[sx][sy][break_cnt]

        for i in range(4):
            nx = sx +dx[i]
            ny = sy +dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and break_cnt == 0 and not visited[nx][ny][1]:
                    q.append((nx,ny,1))
                    visited[nx][ny][1] = visited[sx][sy][0] + 1
                elif arr[nx][ny] == 0 and not visited[nx][ny][break_cnt]:
                    q.append((nx,ny,break_cnt))
                    visited[nx][ny][break_cnt] = visited[sx][sy][break_cnt] + 1
    return 0



res = bfs(0,0)
if res:
    print(res)
else:
    print(-1)