import sys
input = sys.stdin.readline


lst = list(map(str, input().rstrip()))
q = []

for i in range(len(lst)):
    a = lst[i]

    if len(q)>3 :
        if ''.join(q[-4:]) == 'PPAP':
            for _ in range(3):
                q.pop()

    q.append(a)

if len(q)>0:
    if ''.join(q[-4:]) == 'PPAP':
        for _ in range(4):
            q.pop()

if len(q) == 1 and ''.join(q[-1:]) =='P':
    print('PPAP')
elif len(q) == 0 :
    print('PPAP')
else:
    print('NP')