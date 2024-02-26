from itertools import combinations

n,m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    arr = list(map(int,input().split()))
    for c in range(n):
        if arr[c] == 1:
            house.append((r,c))
        elif arr[c] == 2:
            chicken.append((r,c))

def find(c):
    result = 0

    for px, py in house:
        tmp = 1e9
        for cx,cy in c:
            tmp = min(tmp, abs(px-cx)+abs(py-cy))
        result += tmp
    return result



can = list(combinations(chicken,m))

res = 1e9
for c in can:
    res = min(res, find(c))

print(res)