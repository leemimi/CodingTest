n = int(input())
arr = list(map(int, input().split()))

res= arr[-1]

for i in range(n-2, -1,-1):
    if arr[i] > res:
        res = arr[i]
    else:
        if res%arr[i]:
            res = (res//arr[i]+1)*arr[i]
            
print(res)