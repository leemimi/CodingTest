n, m = map(int, input().split())


def dfs(L,S):
    global cnt
    if L == m:
        for k in res:
            print(k, end= ' ')
        print()
    else:
        for i in range(S, n+1):
            res[L] = i
            dfs(L+1, i+1)


res=[0]*m
cnt = 0
dfs(0,1)