n = int(input())

btree = list(map(int, input().split()))
atree = list(map(int, input().split()))

arr =[]

for i in range(n):
    arr.append((btree[i], atree[i]))

arr.sort(key=lambda x:x[1])

ans = 0
for i in range(n):
    ans += arr[i][0] + arr[i][1]*i
print(ans)