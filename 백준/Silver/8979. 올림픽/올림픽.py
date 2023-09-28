n,k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


arr.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)


idx = [arr[i][0] for i in range(n)].index(k)

for i in range(n):
    if arr[idx][1:] == arr[i][1:]:
        print(i+1)
        break
