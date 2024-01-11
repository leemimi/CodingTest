import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a,b,c,d = map(int, input().split())
    a*=100
    c*=100
    arr.append((a+b, c+d))

arr.sort()

target = 301
end = 0
cnt = 0
while arr:
    if target >= 1201 or arr[0][0] > target:
        break
    for i in range(len(arr)):
        if target >= arr[0][0]:
            if end <= arr[0][1]:
                end = arr[0][1]
            arr.pop(0)
        else:
            break
    target = end
    cnt+=1

if target < 1201:
    print(0)
else:
    print(cnt)
