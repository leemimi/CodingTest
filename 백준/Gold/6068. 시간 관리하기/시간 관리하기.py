import sys
input = sys.stdin.readline


n = int(input())
work = []
for _ in range(n):
    t, s = map(int, input().split())
    work.append((t, s))

work.sort(key= lambda x:x[1],reverse=True)
now = float('inf')
for i in range(1,n):
    t,e = work[i][0], work[i][1]

    now = min(now, e)-t

if now <0:
    print(-1)
else:
    print(now)