def light(arr, mid):
    if arr[1] - arr[0] >mid:
        return 0
    if arr[-1] -arr[-2] > mid:
        return 0
    for i in range(1, len(arr)-2):
        if (arr[i+1] - arr[i])/2 >mid:
            return 0
    return 1

n = int(input())
m = int(input())
arr = [0] +list(map(int, input().split())) +[n]

road = [0]*n

lt = 0
rt = n
res = 0
while lt<=rt:
    mid = (lt+rt)//2

    if light(arr,mid):
        rt = mid -1
        res = mid
    else:
        lt = mid+1
print(res)