T = int(input())
for t in range(1,T+1):
    n,m = map(int, input().split())
    binary = bin(m)[2:][::-1]
    ans = "OFF"

    if binary[:n] == '1'*n:
        ans = "ON"

    print(f'#{t} {ans}')
