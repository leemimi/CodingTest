from collections import deque

n,l  = map(int,input().split())
arr = list(map(int,input().split()))
tmp = deque([])
for i in range(n):

    if tmp and tmp[0][0] <= i-l:
        tmp.popleft()
    while len(tmp) >=1 and arr[i] <tmp[-1][1]:
        tmp.pop()

    tmp.append((i,arr[i]))
    print(tmp[0][1], end=" ")
