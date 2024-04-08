import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

minum = abs(100-n)
if n == 100:
    print(0)
else:

    for num in range(0, 999999):
        c = str(num)
        for nn in c:
            if int(nn) in arr:
                break
        else:
            minum = min(minum, abs(n-num)+len(c))

    print(minum)
