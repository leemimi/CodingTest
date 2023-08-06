n,m = map(int,input().split())

lg = []
for _ in range(n):
    lg.append(int(input()))

lt=1
rt=max(lg)

while lt<=rt:
    mid = (lt+rt)//2
    cnt=0
    for i in lg:
        cnt += i//mid
    if cnt>=m:
        lt = mid+1
    else:
        rt = mid-1
print(rt)