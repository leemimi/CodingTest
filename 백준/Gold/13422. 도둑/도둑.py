T = int(input())
for _ in range(T):
    n,m,k = map(int,input().split())
    arr = list(map(int,input().split()))
    answer = 0
    if n == m:
        if sum(arr) < k:
            answer =1 

    else:
        arr += arr
    #m까지의 합
        tmp = sum(arr[:m])    
        for i in range(n):
            if tmp < k:
                answer +=1
            tmp += arr[i+m]
            tmp -= arr[i]

    print(answer)