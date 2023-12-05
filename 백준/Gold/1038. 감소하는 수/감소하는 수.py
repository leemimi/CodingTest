from itertools import combinations
n = int(input())

res = []

for i in range(1,11):
    for j in combinations(range(0,10),i):
        com = list(sorted(j, reverse=True))
        com = ''.join(map(str,com))
        res.append(int(com))

res.sort()
try:
    print(res[n])
except:
    print(-1)