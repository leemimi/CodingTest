
n,s = map(int, input().split())
arr = list(map(int, input().split()))

def dfs(L,cnt):
    global res
    if L >= n:
        return
    cnt += arr[L]

    if cnt == s:
        res+=1

    dfs(L+1, cnt)
    dfs(L+1, cnt - arr[L])


res = 0
dfs(0,0)
print(res)