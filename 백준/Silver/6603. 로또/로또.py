def dfs(L, i):
    if L == 6:
        print(*res)
        return

    for i in range(i, k):
        if L + k - i <6 :
            return
        res.append(arr[i])
        dfs(L+1, i+1)
        res.pop()




while True:

    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break
    arr = arr[1:]
    res = []
    dfs(0,0)
    print()