n = int(input())
m = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

now = m
ans = m
for i in range(n):
    a,b = arr[i]
    now += a
    now -= b
    if now <0:
        ans = 0
        break
    if ans < now:
        ans = now

print(ans)