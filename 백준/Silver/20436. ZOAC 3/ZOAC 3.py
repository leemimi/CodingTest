left ='qwertasdfgzxcv'
right = 'yuiophjklbnm'
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
l,r = map(str,input().split())
word = input()
sum_d =0
xl,yl,xr,yr = None,None,None,None

def find_key (x):
    for i in range(len(keyboard)):
        if x in keyboard[i]:
            a,b = i,keyboard[i].index(x)
    return a,b

for i in range(len(keyboard)):
    if l in keyboard[i]:
        xl,yl =i, keyboard[i].index(l)

    if r in keyboard[i]:
        xr,yr =i, keyboard[i].index(r)


for x in word:
    sum_d+=1
    if x in left:
        a, b=find_key(x)
        d = abs(xl-a)+abs(yl-b)
        xl,yl = a,b
    elif x in right:
        a, b = find_key(x)
        d = abs(xr - a) + abs(yr - b)
        xr,yr =a,b
    sum_d +=d

print(sum_d)