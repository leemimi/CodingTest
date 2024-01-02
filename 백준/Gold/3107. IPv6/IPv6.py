import sys
input = sys.stdin.readline

ip = input().rstrip().split(':')
res = []
check = False
for a in ip:
    if a == '' and not check:
        res += ['0000'for _ in range(8-len(ip)+1)]
        check = True
    else:
        res.append(a.zfill(4))

print(':'.join(res))