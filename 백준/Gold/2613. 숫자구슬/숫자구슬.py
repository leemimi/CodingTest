n,m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)
ans = 0
group = []
while start <= end:
    mid = (start+end)//2

    gnt = 0
    idx =0
    group = []

    while idx<n:
        sub_sum = 0
        sub_cnt = 0
        while idx<n and sub_sum + arr[idx] <=mid:
            sub_sum += arr[idx]
            sub_cnt +=1
            idx +=1
            if m - gnt == n - (idx -1):
                break
        gnt +=1
        group.append(sub_cnt)

    if gnt <= m:
        end -=1
    else:
        start +=1
    ans = mid

print(ans)
print(*group)