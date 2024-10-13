n = int(input())
arr = list(map(int, input().split()))

visited = [0]*n
answer = 0
def dfs(L, ans, ws):
    global answer
    if len(ws) ==2:
        answer = max(answer, ans)
        return

    for i in range(1, len(ws)-1):
        tmp = ws[i-1]*ws[i+1]
        v = arr.pop(i)
        dfs(L+1, ans+tmp, ws)
        ws.insert(i, v)



dfs(0,0, arr)
print(answer)