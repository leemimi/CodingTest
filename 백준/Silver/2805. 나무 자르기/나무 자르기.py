n,m = map(int,input().split())

tree = list(map(int,input().split()))
lt=0
rt=max(tree)
tree.sort()
while lt<=rt:
    mid=(lt+rt)//2
    cnt =0
    for x in tree:
        if x> mid:
            cnt+=x-mid
    if cnt >= m:
        lt = mid+1
    else:
        rt = mid-1
print(rt)