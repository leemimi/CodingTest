n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = 0
for i in range(n-2):
    lt = i+1
    rt = n-1
    while lt<rt:
        total = arr[lt]+arr[rt]
        
        if total == -arr[i]:
            if arr[lt] == arr[rt]:
                ans += rt - lt
                lt+=1
            else:
                j,k = lt, rt
                while arr[j] == arr[lt] and j<rt:
                    j+=1
                while arr[k] == arr[rt] and k > lt:
                    k-=1
                ans += (j-lt)*(rt-k)
                lt = j
                rt = k
        elif total < -arr[i]:
            lt+=1
        else:
            rt-=1
print(ans)