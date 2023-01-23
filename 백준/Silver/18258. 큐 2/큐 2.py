import sys
from collections import deque

n = int(input())
arr = deque()

for _ in range(n):
    a = sys.stdin.readline().split()
    if a[0]=='push':
        arr.append(a[1])
    elif a[0] =='pop':
        if len(arr) == 0:
            print(-1)
        else :
            cur = arr.popleft()
            print(cur)
    elif a[0]=='size':
        print(len(arr))
    elif a[0] =='empty':
        if len(arr)==0:
            print(1)
        else:
            print(0)
    elif a[0]=='front':
        if len(arr)==0:
            print(-1)
        else:
            print(arr[0])
    elif a[0]=='back':
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])
