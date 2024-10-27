import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

k = 0
lt = min(arr)
rt = sum(arr)
while lt<=rt:
    mid = (lt+rt)//2

    use = 1
    tmp = mid
    for i in range(n):
        if arr[i] > tmp:
            use+=1
            tmp = mid

        tmp = tmp - arr[i]

    if use > m or mid < max(arr):
        lt = mid +1
    else:
        rt = mid -1
        k = mid

print(k)