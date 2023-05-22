import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(a):
    if a == arr[a]:
        return a
    arr[a] = find(arr[a])
    return arr[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b: 
        return
    if a < b:
        arr[b] = a 
    else:
        arr[a] = b 

n = int(input())
m = int(input())

arr = [i for i in range(n+1)]
for i in range(1,n+1):
    maps = list(map(int, input().split()))
    for j in range(1,len(maps)+1):
        if maps[j-1]==1:
            union(i,j)

trip = list(map(int,input().split()))
result = set([find(i) for i in trip])

if len(result) != 1:
    print("NO")
else:
    print("YES")