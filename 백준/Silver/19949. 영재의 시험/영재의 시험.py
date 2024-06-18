import sys
sys.setrecursionlimit(100000)

arr = list(map(int, input().split()))
res = 0

def dfs(L, solve, cnt):
    global res
    if L == 10:
        res+=1
        return


    for j in range(1,6):
        if len(solve) <2 or (solve[-1]!=solve[-2] or solve[-1]!=j):
            solve.append(j)
            if arr[len(solve)-1] == j:
                dfs(L+1,solve, cnt+1)
            else:
                if len(solve) - cnt > 5 :
                    solve.pop()
                    continue
                dfs(L+1,solve,cnt)
            solve.pop()


dfs(0,[], 0)
print(res)