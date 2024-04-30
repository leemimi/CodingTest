import sys
input = sys.stdin.readline
t = int(input())

def tree(node,cnt):
    global arr
    visited[node] = True
    for v in arr[node]:
        if not visited[v]:
            cnt = tree(v,cnt+1)
    return cnt


for _ in range(t):
    res = 0
    n,m = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    visited[0] = True
    for _ in range(m):
        a,b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    res = tree(1,0)
    print(res)