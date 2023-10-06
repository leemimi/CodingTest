import sys
input = sys.stdin.readline
n,x = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
res = 0


if sum(arr) == 0:
    print("SAD")

else:

    val = sum(arr[:x])
    res = val
    cnt = 1

    for i in range(x,n):
        val += arr[i]
        val -= arr[i-x]

        if val > res:
            res = val
            cnt = 1
        elif val == res:
            cnt+=1

    print(res)
    print(cnt)