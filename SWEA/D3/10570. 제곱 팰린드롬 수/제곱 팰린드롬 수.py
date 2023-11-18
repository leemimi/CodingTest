T = int(input())
for t in range(1,T+1):
    a,b = map(int, input().split())
    ans = 0
    for i in range(a,b+1):
        tmp = int(i**0.5)
        if (tmp**2) == i:
            if str(i) == str(i)[::-1] and str(tmp) == str(tmp)[::-1]:
                ans +=1



    print(f'#{t} {ans}')