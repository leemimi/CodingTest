import sys
input = sys.stdin.readline

n,m = map(int, input().split())

T = []
for _ in range(n):
    t = int(input())
    T.append(t)
lt = min(T)
rt = max(T)*m
result = rt

while lt<=rt:
    mid = (lt+rt)//2
    cnt = 0
    for i in range(n):
        cnt += mid//T[i]

    if cnt >= m:
        rt = mid -1
        result = min(result, mid)
    else:
        lt = mid +1

print(result)