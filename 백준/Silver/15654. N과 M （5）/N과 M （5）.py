n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
def dfs():
    if len(res) == m:
        for k in res:
            print(k, end=' ')
        print()
    for i in range(n):
        if arr[i] not in res:
            res.append(arr[i])
            dfs()
            res.pop()

res = []
dfs()