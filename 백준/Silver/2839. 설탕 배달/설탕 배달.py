import sys
n = int(input())
res = 0

if n%5==0:
    res = n//5
    print(res)
else:
    while n>0:
        n -= 3
        res +=1
        if n%5==0:
            res += n//5
            print(res)
            break
        elif n == 1 or n ==2:
            print(-1)
            break
        elif n == 0 :
            print(res)
            break