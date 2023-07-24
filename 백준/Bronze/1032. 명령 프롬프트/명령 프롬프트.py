n = int(input())
arr = []
for _ in range(n):
    s = input()
    arr.append(s)

ans = list(arr[0])
for i in range(1,n):
    for j in range(len(arr[i])):
        if ans[j] != arr[i][j]:
            ans[j] ='?'
        else:
            continue
print(''.join(ans))