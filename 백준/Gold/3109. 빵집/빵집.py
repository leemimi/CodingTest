import sys
input = sys.stdin.readline

dx = [-1, 0, 1]
dy = [1, 1, 1]
def dfs(x,y):
    global res
    arr[x][y] = 'o'
    if y==c-1:
        res+=1
        return True
    for k in range(3):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<r and 0<=ny<c :
            if arr[nx][ny] != 'x' and arr[nx][ny] != 'o':
                if dfs(nx,ny):
                    return True

r,c = map(int,input().split())
arr = []
for _ in range(r):
    arr.append(list(input().strip()))

res = 0
for i in range(r):
    dfs(i,0)
print(res)