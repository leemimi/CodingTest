p,m = map(int, input().split())
arr = []
room = []
for _ in range(p):
    level,name = input().split()
    if not room:
        room.append([[int(level),name]])
        continue
    enter = False
    for r in room:
        if len(r)<m and r[0][0] -10 <= int(level) <= r[0][0] + 10:
            r.append([int(level),name])
            enter = True
            break
    if not enter:
        room.append([[int(level),name]])

for r in room:
    r.sort(key=lambda x:x[1])

for r in room:
    if len(r) == m:
        print('Started!')
    else:
        print('Waiting!')
    for lv,n in r:
        print(lv, n)