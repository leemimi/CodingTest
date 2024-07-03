import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

res = 0
minus = []
plus = []
last = 0
for i in range(n):
    last = max(abs(arr[i]), last)
    if arr[i] < 0:
        minus.append(arr[i])
    else:
        plus.append(arr[i])

minus.sort()
plus.sort(reverse=True)


for i in range(0,len(minus),m):
    res += abs(minus[i])*2
for i in range(0, len(plus), m):
    res += plus[i]*2
print(res - last)