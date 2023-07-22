import sys
n,m = map(int,input().split())
arr=list(map(int, input().split()))
lt = 0
rt = 0
sum = 0
min_length = sys.maxsize
while True:
    if sum >= m:
        min_length = min(min_length, rt-lt)
        sum -= arr[lt]
        lt+=1
    elif rt ==n:
        break
    else:
        sum += arr[rt]
        rt +=1

if min_length ==sys.maxsize:
    print(0)
else:
    print(min_length)
