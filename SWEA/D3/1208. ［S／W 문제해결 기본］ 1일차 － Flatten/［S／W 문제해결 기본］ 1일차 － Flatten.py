T = 10
for t in range(1, T + 1):
    dump = int(input())
    arr = list(map(int, input().split()))

    top = max(arr)
    idx = arr.index(top)
    bottom = min(arr)
    idx1 = arr.index(bottom)

    res = 0

    for _ in range(dump):
        arr[arr.index(max(arr))] -=1
        arr[arr.index(min(arr))] +=1

        res = max(arr) - min(arr)
        if res <=1:
            break

    print(f"#{t} {res}")
