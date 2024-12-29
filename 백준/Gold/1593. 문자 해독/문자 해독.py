w,g = map(int, input().split())
word = input()
S = input()
cnt = 0

wl =[0]*52
sl = [0]*52

for i in range(w):
    if 'a' <= word[i] <='z':
        wl[ord(word[i])- ord('a')]+=1
    else:
        wl[ord(word[i])-ord('A')+26]+=1

lt =0
rt =0
for i in range(g):
    if 'a'<= S[i] <='z':
        sl[ord(S[i])-ord('a')]+=1
    else:
        sl[ord(S[i])-ord('A')+26]+=1
    rt+=1
    if rt == w:
        if wl == sl:
            cnt+=1
        if 'a'<= S[lt] <='z':
            sl[ord(S[lt]) - ord('a')] -= 1
        else:
            sl[ord(S[lt])-ord('A')+26]-=1
        rt-=1
        lt+=1
print(cnt)