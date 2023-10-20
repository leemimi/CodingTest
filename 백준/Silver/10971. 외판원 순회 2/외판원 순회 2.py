import sys
input = sys.stdin.readline

def dfs(start, now ,sum, cnt):
    global res

    if  cnt == n:
        if arr[now][start]:
            sum += arr[now][start]
            res = min(res, sum)
        return

    if sum > res:
        return

    for k in range(n):
        if not visited[k] and arr[now][k]:
            visited[k] = 1
            dfs(start, k, sum+ arr[now][k], cnt+1)
            visited[k] = 0

n =int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
res = sys.maxsize
visited = [0] * n
for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0

print(res)