import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)

def dfs(v):
    global arr

    visited[v] = True


    for i in arr[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

cnt = 0
visited = [False]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)