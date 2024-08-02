import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n,k = map(int, input().split())
    arr= list(map(int, input().split()))
    arr.sort()
    lt =0
    rt =n-1
    cnt = 0
    minsize = 200000002
    while lt<rt:
        sums = arr[lt]+arr[rt]

        if minsize > abs(k-sums):
            minsize = abs(k-sums)
            cnt = 0
        if sums < k:
            if minsize == abs(k-sums):
                cnt+=1
            lt+=1
        elif sums >k:
            if abs(k-sums) == minsize:
                cnt+=1
            rt-=1
        else:
            cnt+=1
            lt+=1

    print(cnt)