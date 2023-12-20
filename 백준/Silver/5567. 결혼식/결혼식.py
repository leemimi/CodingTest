n = int(input())
m = int(input())
arr = [[]*(n+1) for _ in range(n+1)]

def dfs(v,L):
    if L == 2:
        return
    visited[v] = 1

    for k in arr[v]:
        if not visited[k]:
            visited[k] = 1
        dfs(k,L+1)



visited = [0]*(n+1)
for _ in range(m):
    a,b =list(map(int, input().split()))
    arr[a].append(b)
    arr[b].append(a)

dfs(1,0)
print(sum(visited)-1)