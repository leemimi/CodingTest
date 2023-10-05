n = int(input())
arr= list(map(int, input().split()))
money = list(map(int,input().split()))

res = money[0] * arr[0]
min_money = money[0]
for i in range(1,n-1):
    if money[i] < min_money:
        min_money = money[i]
    res += min_money * arr[i]
print(res)