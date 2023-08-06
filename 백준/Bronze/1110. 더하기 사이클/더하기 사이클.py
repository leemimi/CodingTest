
n = int(input())
s = ''
if n < 10:
    n = str(n)
    s='0'+n
else:
    s = str(n)


cnt = 0
ans = int(s)
while True:
    new_num = int(s[0])+int(s[1])
    s = s[1]+str(new_num)[-1]
    cnt+=1

    if int(s) == ans:
        print(cnt)
        break