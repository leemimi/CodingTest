t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()
    idx = 0
    res = 0
    for i in range(len(a)):
        while idx <m:
            if a[i] > b[idx]:
                idx+=1
            else:
                break
        res += idx
    print(res)