n,k =map(int,input().split())
S = list(map(int, input().split()))

lt = 0
rt = 0
cnt, res = 0, 0
while rt < n:

    if cnt > k:
        if S[lt] %2 != 0:
            cnt -=1
        lt +=1
        continue
    else:
        if S[rt]%2!=0:
            cnt +=1
        rt+=1

    res = max(res, rt-lt-cnt)
print(res)