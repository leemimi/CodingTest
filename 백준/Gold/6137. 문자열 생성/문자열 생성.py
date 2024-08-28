n = int(input())
s= []
for _ in range(n):
    s.append(input())

lt=0
rt=len(s)-1
T=""
while lt<=rt:
    if s[lt] < s[rt]:
        T+=s[lt]
        lt+=1
    elif s[lt] > s[rt]:
        T+=s[rt]
        rt-=1
    else:
        l=lt+1
        r=rt-1
        flag= 0
        while l<=r:
            if s[l]<s[r]:
                flag= 1
                break
            elif s[l]>s[r]:
                flag =2
                break
            l+=1
            r-=1
        if flag ==1:
            T+=s[lt]
            lt+=1
        else:
            T+=s[rt]
            rt-=1
answer = list(T)
cnt=0
for a in answer:
    print(a,end="")
    cnt+=1
    if cnt%80==0:
        print()