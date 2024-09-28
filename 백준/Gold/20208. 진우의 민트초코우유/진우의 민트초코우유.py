import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M, H = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]

answer = 0

def dfs(x,y,health,visited, cnt):
    global answer, mint, hx, hy, H
    if answer == len(mint):
        return
    tmp = abs(x - hx) + abs(y - hy)
    if health >= tmp:
        answer = max(answer, cnt)
    for i in range(len(mint)):
        if visited[i]: continue
        mx,my = mint[i]
        t = abs(mx - x) + abs(my - y)
        if health - t >=0:
            visited[i] = True
            dfs(mx,my,health-t+H,visited,cnt+1)
            visited[i] = False
    return




hx, hy = 0,0
mint = []
visited = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            hx = i
            hy = j
        elif arr[i][j] == 2:
            mint.append((i,j))

visited = [False]*len(mint)
dfs(hx,hy,M,visited,0)

print(answer)