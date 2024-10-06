import sys
input = sys.stdin.readline


n,m,h = map(int, input().split())
arr = [[False]*n for _ in range(h)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a-1][b-1] = True

def check():
    for start in range(n):
        now = start
        for j in range(h):
            if arr[j][now] == True:
                now+=1
            elif now>0 and arr[j][now-1] == True:
                now-=1
        if now!=start:
            return False
    return True



def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3 or ans<=cnt:
        return


    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0
        for j in range(now,n-1):
            if not arr[i][j] and not arr[i][j+1]:
                if j>0 and arr[i][j-1]:
                    continue
                arr[i][j] = True
                dfs(cnt+1, i, j+2)
                arr[i][j] = False

ans = 4
dfs(0,0,0)
print(ans if ans<4 else -1)