import sys
sys.setrecursionlimit(100000)

arr = list(map(int, input().split()))
res = 0

def dfs(L, solve, cnt):
    global res
    if L == 10:
        for i in range(len(arr)):
            if solve[i] == arr[i]:
                cnt+=1
        if cnt >= 5:
            res+=1
        return


    for j in range(1,6):
        if L >1 and solve[-1] == solve[-2] == j:
            continue
        solve.append(j)
        dfs(L+1, solve, cnt)
        solve.pop()

dfs(0,[], 0)
print(res)