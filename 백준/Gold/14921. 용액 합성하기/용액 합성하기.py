n = int(input())
arr = list(map(int, input().split()))

lt = 0
rt = n-1
res = int(1e9)
while lt < rt:
    tmp = arr[lt] + arr[rt]
    if abs(res) >  abs(tmp):
        res = tmp
    if tmp == 0 :break
    elif tmp > 0 : rt -=1
    else:
        lt +=1

print(res)