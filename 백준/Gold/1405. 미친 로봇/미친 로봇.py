N,e,w,n,s = list(map(int, input().split()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
data = [e,w,s,n]

arr = [[0]*(2*N+1) for _ in range(2*N+1)]
ans = 0

def dfs(x,y,pes,cnt):
    global ans

    if cnt == N:
        ans+=pes
        return

    np = pes
    arr[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<(2*N+1) and 0<=ny<(2*N+1):
            if arr[nx][ny] == 1:
                continue

            else:
                dfs(nx,ny,np*(data[i]/100),cnt+1)
                arr[nx][ny] = 0

dfs(N,N,1,0)
print(ans)