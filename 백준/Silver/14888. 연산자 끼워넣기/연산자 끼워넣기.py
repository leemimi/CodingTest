n = int(input())
arr = list(map(int, input().split()))
s = list(map(int, input().split()))
res = []
def bt(L,sum, add, sub, mul, div):
    global res
    if L == n:
        res.append(sum)
        return
    if add :
        bt(L+1,sum+arr[L],add-1, sub, mul, div)
    if sub:
        bt(L+1, sum-arr[L],add, sub-1, mul, div)
    if mul:
        bt(L+1, sum*arr[L],add, sub, mul-1, div)
    if div:
        bt(L+1, int(sum/arr[L]), add, sub, mul, div-1)


bt(1,arr[0], s[0], s[1],s[2],s[3])
print(max(res))
print(min(res))