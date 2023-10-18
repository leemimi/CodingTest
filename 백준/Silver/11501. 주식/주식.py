import sys
input = sys.stdin.readline
t =int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0

    max = 0
    for i in range(n-1,-1,-1):
        if arr[i] > max:
            max = arr[i]
        else:
            res += max - arr[i]

    print(res)