import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)
def dfs(prev, node):
    global isTree
    visited[node] = True


    for j in arr[node]:
        if j == prev:
            continue
        if visited[j]:
            isTree = False
            return
        dfs(node,j)


cnt = 0
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    ans = 0
    cnt += 1
    arr = [[] for _ in range(n + 1)]
    for _ in range(m):
        a,b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    visited = [False]*(n+1)
    for i in range(1, n+1):
        if visited[i]:
            continue

        isTree = True
        dfs(0,i)
        if isTree:
            ans+=1

    if ans == 1:
        print(f"Case {cnt}: There is one tree.")
    elif ans == 0:
        print(f"Case {cnt}: No trees.")
    else:
        print(f"Case {cnt}: A forest of {ans} trees.")