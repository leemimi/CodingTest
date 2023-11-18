T = int(input())
for t in range(1,T+1):
    n,a,b = map(int, input().split())

    r1,r2 = 0,0

    if a+b >= n:
        r2 = abs(n - (a+b))
    r1 = min(a,b)

    print(f'#{t} {r1} {r2}')