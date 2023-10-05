n = int(input())
arr= list(map(int, input().split()))
money = list(map(int,input().split()))

res = money[0] * arr[0]
road = sum(arr[1:])

min_money = min(money[:n-1])

res += road*min_money

print(res)