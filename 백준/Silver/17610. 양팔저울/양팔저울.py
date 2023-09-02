n = int(input())
arr = list(map(int, input().split()))

def dfs(L,sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)

    else:
        dfs(L+1, sum+arr[L])
        dfs(L+1, sum-arr[L])
        dfs(L+1, sum)


s = sum(arr)
res = set()
dfs(0,0)
print(s - len(res))