import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int, input().split())
ans = 0
arr = []
for _ in range(r):
    arr.append(list(input()))
visited = set()


def dfs(x,y,cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and not arr[nx][ny] in visited:
            visited.add(arr[nx][ny])
            dfs(nx,ny,cnt+1)
            visited.remove(arr[nx][ny])
visited.add(arr[0][0])
dfs(0,0,1)
print(ans)