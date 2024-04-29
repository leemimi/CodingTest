import sys
input = sys.stdin.readline

arr = [0]
n = int(input())
for i in range(n):
    arr.append(int(input()))
ans = set()
up = []
down = []
def dfs(L, up, down):
    up.add(L)
    down.add(arr[L])

    if arr[L] in up:
        if up == down:
            ans.update(up)
        return
    return dfs(arr[L], up, down)
for i in range(n):
    if i+1 not in ans:
        dfs(i+1, set(), set())
print(len(ans))
ans = list(ans)
ans.sort()
for a in ans:
    print(a)