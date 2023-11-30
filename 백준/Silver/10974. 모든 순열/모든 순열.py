def dfs(L):
    if L == n:
        print(*visited)
    else:
        for i in range(n):
            if i+1 in visited:
                continue
            else:
                visited[L] = i+1
                dfs(L+1)
                visited[L] = 0


n = int(input())
visited = [0]*n
dfs(0)