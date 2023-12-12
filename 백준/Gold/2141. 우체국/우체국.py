n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

midnum = 0

for i in range(len(arr)):
    midnum += arr[i][1]

now = 0
for i in range(n):
    now += arr[i][1]
    if now >= midnum/2:
        print(arr[i][0])
        break