h,w = map(int,input().split())
arr = list(map(int, input().split()))

res = 0

for i in range(1,w-1):
    tmp = min(max(arr[:i]), max(arr[i+1:]))
    if tmp > arr[i]:
        res += tmp - arr[i]
print(res)