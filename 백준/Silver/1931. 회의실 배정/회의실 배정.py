import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a,b = map(int, input().split())
    arr.append((a,b))
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

cnt,last = 0,0
for start,end in arr:
    if start >= last:
        cnt+=1
        last = end
print(cnt)