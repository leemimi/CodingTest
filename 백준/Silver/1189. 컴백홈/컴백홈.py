r,c,k = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
cnt = 0

state = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(L,a,b):
    global cnt
    if L == k and a == 0 and b == c-1:
        cnt+=1
    else:
        visited[a][b] = 1
        for i in range(4):
            nx = dx[i]+a
            ny = dy[i]+b
            if 0<=nx<r and 0<=ny<c and arr[nx][ny] != 'T':
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(L+1,nx,ny)
                    visited[nx][ny] = 0


dfs(1,r-1,0)
print(cnt)