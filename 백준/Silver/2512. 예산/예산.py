import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())


arr.sort()
lt = 1
rt = arr[n-1]

ans = 0
while lt<=rt:
    mid = (lt+rt)//2

    res = 0

    for i in range(len(arr)-1,-1,-1):
        if arr[i] > mid :
            res +=  mid
        else:
            res += arr[i]

    if res > m:
        rt = mid -1

    else:
        lt = mid + 1
print(rt)
