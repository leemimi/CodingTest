
n,m = map(int,input().split())

def dfs():
    if len(res) == m:
        print(' '.join(map(str,res)))
    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i] = True
        res.append(i)
        dfs()
        res.pop()
        visited[i] = False

res = []
visited = [False] * (n+1)
dfs()
