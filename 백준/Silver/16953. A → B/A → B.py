a,b = map(int, input().split())

cnt = 0
while a!=b:
    if a>b:
        cnt = -2
        break
    elif str(b)[-1] == '1':
        b = b//10
        cnt +=1
    elif b%2==0:
        b = b//2
        cnt+=1
    else:
        cnt =-2
        break
print(cnt+1)