n = int(input())
S = int(input())
sr = input()

p = 'IOI'
sub = 'OI'
if n >1 :
    for i in range(n-1):
        p +=sub

idx = 0
cnt = 0
for i in range(S):
    if sr[i:i+len(p)] == p:
        cnt+=1

print(cnt)