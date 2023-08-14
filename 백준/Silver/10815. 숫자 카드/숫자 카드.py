n = int(input())
arr = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
arr.sort()
ans = []
for i in range(m):
    lt = 0
    rt = n-1
    while lt <= rt:
        mid = (lt+rt)//2
        if arr[mid] > nums[i]:
            rt = mid - 1
        elif arr[mid] == nums[i]:
            ans.append(1)
            break
        else:
            lt = mid +1
    if lt > rt:
        ans.append(0)

print(*ans)