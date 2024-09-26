import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
days = []

for i in range(n):
    m, *rice = map(int, input().split())
    days.append(rice)

visited = [[0]*10 for _ in range(n+1)]

def dfs(L,yesterday, cake):
    global flag
    if flag:
        return

    if L == n:
        for c in cake:
            print(int(c))
        flag = True
        return


    for i in days[L]:
        if L==0:
            visited[L+1][i] = 1
            dfs(L+1,i,cake+str(i))

        elif yesterday != i and not visited[L+1][i]:
            visited[L+1][i] = 1
            dfs(L+1, i, cake+str(i))
    return
flag = False
dfs(0,0,'')
if not flag:
    print(-1)
