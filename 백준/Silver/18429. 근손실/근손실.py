import sys
n,k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
def dfs(L, sums):
    global cnt
    if sums<500:
        return
    if L == n:
        cnt+=1
        return
    sums -=k
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(L+1,sums+arr[i])
            visited[i] = 0


visited = [0]*n
dfs(1, 500)
print(cnt)