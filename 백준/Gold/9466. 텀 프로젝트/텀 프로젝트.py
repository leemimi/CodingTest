import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(x):
    global res
    visited[x] = True
    cycle.append(x)
    number = arr[x]

    if visited[number]:
        if number in cycle:
            res += cycle[cycle.index(number):]
            return
    else:
        dfs(number)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [True] + [False]*n
    res = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n-len(res))