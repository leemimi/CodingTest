n,s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
ans = []
def dfs(idx):
    global cnt,ans
    if sum(ans) == s and len(ans)>0:
        cnt+=1

    for i in range(idx,n):
        ans.append(arr[i])
        dfs(i+1)
        ans.pop()


dfs(0)
print(cnt)