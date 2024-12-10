n,k = map(int, input().split())
arr = []
for _ in range(n):
    g,x = map(int,input().split())
    arr.append((x,g))

arr.sort()

ans = 0
tmp = 0
lt = 0
rt = 0

while lt<=rt and rt<n:
    if arr[rt][0] - arr[lt][0] <= 2*k:
        tmp += arr[rt][1]
        ans = max(tmp, ans)
        rt+=1
    else:
        tmp -= arr[lt][1]
        lt+=1
print(ans)