n,b,w = map(int,input().split())
arr = list(map(str,input().rstrip()))

answer = 0

lt = 0
rt = 0

wcnt = 0
bcnt = 0


while rt < n:
    if arr[rt] == 'W':
        wcnt += 1
    else:
        bcnt += 1

    if bcnt > b :
        if arr[lt] == 'W':
            wcnt -= 1
        else:
            bcnt -= 1
        lt += 1

    if wcnt >= w :
        answer = max(answer, rt - lt + 1)
    rt += 1

print(answer)