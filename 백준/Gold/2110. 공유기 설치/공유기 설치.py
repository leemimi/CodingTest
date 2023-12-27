import sys
input=sys.stdin.readline
N, C = map(int,input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()

lt = 1
rt = arr[-1] - arr[0]
ans = 0
while lt<=rt:
    mid = (lt+rt)//2
    cur = arr[0]
    cnt = 1

    for i in range(1,len(arr)):
        if arr[i] - cur >= mid:
            cnt+=1
            cur = arr[i]
    if cnt >= C:
        ans = mid
        lt = mid+1
    else:
        rt = mid -1

print(ans)
