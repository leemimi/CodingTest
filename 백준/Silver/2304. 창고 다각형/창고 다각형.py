import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    L,H =map(int, input().split())
    arr.append((L,H))

arr.sort(key=lambda x:x[0])

res = 0
i = 0
for l in arr :
    if l[1] >res :
        res = l[1]
        idx = i
    i += 1
height = arr[0][1]

for i in range(idx):
    if height < arr[i+1][1]:
        res += height*abs(arr[i][0]-arr[i+1][0])
        height = arr[i+1][1]
    else:
        res += height*abs(arr[i][0]- arr[i+1][0])
height = arr[-1][1]

for i in range(n-1,idx,-1):
    if height < arr[i-1][1]:
        res += height*abs(arr[i][0]-arr[i-1][0])
        height = arr[i-1][1]
    else:
        res += height*abs(arr[i][0]- arr[i-1][0])

print(res)