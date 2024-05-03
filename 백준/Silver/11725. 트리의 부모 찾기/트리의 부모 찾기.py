import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(node):

    for v in arr[node]:
        if not visited[v]:
            visited[v] = node
            dfs(v)




n = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(n+1)
dfs(1)
for x in range(2, n+1):
    print(visited[x])