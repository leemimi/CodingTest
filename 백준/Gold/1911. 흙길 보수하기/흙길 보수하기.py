import sys
input = sys.stdin.readline

n,L = map(int, input().split())
arr = []
for _ in range(n):
    a,b = map(int, input().split())
    arr.append((a,b))

arr.sort(key=lambda x:x[0])
cur = 0
cnt = 0
for start, end in arr:
    if cur > start:
        start = cur
    while start < end:
        start+=L
        cnt+=1
    cur = start
print(cnt)