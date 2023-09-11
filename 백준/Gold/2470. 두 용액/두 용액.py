n = int(input())
arr = list(map(int, input().split()))
lt = 0
rt = n-1

arr.sort()
res = [arr[lt],arr[rt]]
ans = abs(arr[lt]+arr[rt])

while lt<rt:
    sum = arr[lt] + arr[rt]

    if abs(sum) < ans:
        ans = abs(sum)
        res = [arr[lt],arr[rt]]
        if ans == 0 :
            break
    if sum < 0 :
        lt +=1
    else:
        rt-=1

print(*res)