p = int(input())
for _ in range(p):
    cnt = 0
    arr = list(map(int, input().split()))
    num = arr[0]
    arr.remove(arr[0])


    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j] :
                arr[i], arr[j] = arr[j], arr[i]
                cnt+=1

    print(num, cnt)