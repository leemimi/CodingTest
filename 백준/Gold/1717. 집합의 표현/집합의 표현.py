import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [i for i in range(n+1)]

def find(a):
    if a == arr[a]:
        return a
    arr[a] = find(arr[a])
    return arr[a]

def union(a,b):
    pa = find(a)
    pb = find(b)
    arr[pa] = pb


for _ in range(m):
    num, a,b = map(int, input().split())
    if num == 0 :
        union(a,b)
    elif num == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

