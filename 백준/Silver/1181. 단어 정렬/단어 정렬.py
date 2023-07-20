n = int(input())
arr = []
for _ in range(n):
    s = input()
    if s in arr:
        continue
    arr.append(s)

arr = sorted(arr)
arr.sort(key=len)

for i in range(len(arr)):
    print(arr[i])