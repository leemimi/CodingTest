import sys

def cal(alst,blst):
    asm=bsm=0
    for i in range(M):
        for j in range(M):
            asm += arr[alst[i]][alst[j]]
            bsm += arr[blst[i]][blst[j]]
    return abs(asm-bsm)
def dfs(n, alst, blst):
    global min_size
    if n == N:
        if len(alst) == len(blst):
            min_size = min(min_size, cal(alst,blst))
        return

    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
min_size = sys.maxsize

M = N//2
dfs(0,[],[])
print(min_size)