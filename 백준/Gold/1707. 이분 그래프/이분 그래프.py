import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    v,e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    def dfs(now, group):
        visited[now] = group
        for i in graph[now]:
            if visited[i] == 0:
                if not dfs(i, -group):
                    return False
            elif visited[i] == visited[now]:
                return False
        return True

    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    res = True
    for  i in range(1,v+1):
        if visited[i] == 0:
            res = dfs(i, 1)
            if not res:
                break
    print("YES") if res else print("NO")