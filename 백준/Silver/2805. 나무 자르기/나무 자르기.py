n,m = map(int, input().split())
tree = list(map(int, input().split()))

tree.sort()

lt = 1
rt = tree[n-1]
result = 0
while lt <= rt:
    mid = (lt+rt)//2
    ans = 0

    for a in tree:
        if a > mid:
            ans += a-mid

    if ans >= m:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(result)