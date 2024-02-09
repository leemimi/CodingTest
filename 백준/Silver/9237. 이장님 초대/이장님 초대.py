
n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

res = []
for i in range(n):
    res.append(arr[i]+1+i)

print(max(res)+1)