import sys

def dfs(cowNum):
    if put[cowNum]:
        return 0
    put[cowNum] = True

    for want in cow[cowNum]:
        if barn[want] == -1 or dfs(barn[want]):
            barn[want] = cowNum
            return 1
    return 0

n,m = map(int, input().split())
cow = [[] + list(map(int, input().split()[1:])) for _ in range(n)]
barn = [-1 for _ in range(m+1)]

for i in range(n):
    put = [False for _ in range(n)]
    dfs(i)

print(m+1 - barn.count(-1))