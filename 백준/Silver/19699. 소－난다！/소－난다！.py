import sys
input = sys.stdin.readline
import math
n,m =map(int, input().split())
arr= list(map(int, input().split()))
li = [0]*m
res = set()

def is_prime(a):
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i == 0:
            return False
    return True

visited = [False]*n
def dfs(L):
    if L == m:
        vailed = is_prime(sum(li))
        if vailed:
            res.add(sum(li))
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        li[L] = arr[i]
        dfs(L+1)
        visited[i] = False

dfs(0)
res = list(res)
res.sort()
if not len(res):
    print("-1")
else:
    for i in range(len(res)):
        print(res[i], end = ' ')