n,k = map(int, input().split())
arr = list(map(int, input().split()))

tmp = [0]*n
res = sum(arr[:k])
sums = sum(arr[:k])
for i in range(n-k):
    sums += arr[i+k] - arr[i]
    if res < sums:
        res = sums


print(res)