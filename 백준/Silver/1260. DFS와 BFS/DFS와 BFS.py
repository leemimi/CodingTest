def dfs(v):
    print(v, end = ' ')
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0  and arr[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visited[v] = 0
    while(queue):
        v = queue[0]
        print(v, end = ' ')
        del queue[0]
        for i in range(1,n+1):
            if visited[i] == 1 and arr[v][i] == 1:
                queue.append(i)
                visited[i] = 0
                

n,m,v = map(int,input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1

dfs(v)
print()
bfs(v)