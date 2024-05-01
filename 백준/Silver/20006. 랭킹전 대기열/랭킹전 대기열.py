import sys
input = sys.stdin.readline

p,m = map(int, input().split())
room = [[] for _ in range(p)]
for _ in range(p):
    l,n = map(str, input().split())
    l = int(l)
    for i in range(len(room)):
        if len(room[i]) < m :
            if len(room[i]) > 0 and (l <=room[i][0][0]+10 and l >= room[i][0][0]-10):
                room[i].append((l,n))
                break
            else:
                if len(room[i]) == 0:
                    room[i].append((l,n))
                    break


for r in room:
    r.sort(key= lambda x:x[1])

for r in room:
    if len(r) == m:
        print("Started!")
    elif len(r) < m and len(r) > 0:
        print("Waiting!")
    if len(r)>0:
        for l,n in r:
            print(l,n)