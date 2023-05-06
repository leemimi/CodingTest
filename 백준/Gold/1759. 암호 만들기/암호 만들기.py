import sys

def back_tracking(cnt, idx):
    if cnt == L:
        vo,co = 0,0
        for i in range(L):
            if ans[i] in cons:
                vo+=1
            else:
                co+=1
        if vo>=1 and co>=2:
            print("".join(ans))
        return
    for i in range(idx,C):
        ans.append(arr[i])
        back_tracking(cnt+1, i+1)
        ans.pop()


L,C = map(int, input().split())
arr = sorted(list(map(str, input().split())))
ans =[]
cons = ['a', 'e', 'i', 'o', 'u']
back_tracking(0,0)
