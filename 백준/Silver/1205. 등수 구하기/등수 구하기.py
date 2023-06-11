n,new,p= map(int,input().split())
if n == 0:
    print(1)
else:
    arr = list(map(int, input().split()))
    if n == p and arr[-1] >= new:
        print(-1)
    else:
        res = n+1
        for i in range(n):
            if  arr[i] <= new :
                res = i+1
                break
        print(res)
