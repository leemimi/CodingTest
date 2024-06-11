import sys
input = sys.stdin.readline

n = int(input())

def dfs(L, s):
    if len(s) == len(alp):
        print(s)
        return

    for d in dict:
        if dict[d]:
            dict[d]-=1
            dfs(dict, s+d)
            dict[d]+=1

for _ in range(n):
    alp = list(input().rstrip())
    alp.sort()
    dict = {}

    for a in alp:
        if a in dict:
            dict[a]+=1
        else:
            dict[a] = 1
    dfs(dict, "")