T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1]*n

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)


    print(f'#{t} {max(dp)}')