import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
ans = 1
if n == 0: print(0)
else:
    for i in range(n):
        if cnt + arr[i] > m:
            cnt = arr[i]
            ans+=1
        else:
            cnt+= arr[i]
    
    print(ans)