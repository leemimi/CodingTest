import sys
input = sys.stdin.readline
from itertools import combinations

n,m,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]



enemies = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            enemies.append((i,j))

archer_positions = list(combinations([(n, j) for j in range(m)], 3))
answer = 0

def find_target(x, y, area):
    min_dist = d + 1
    target = (-1, -1)
    for i in range(n):
        for j in range(m):
            if area[i][j] == 1:
                dist = abs(x - i) + abs(y - j)
                if dist <= d:
                    # 거리 우선, 왼쪽 우선으로 갱신
                    if dist < min_dist or (dist == min_dist and j < target[1]):
                        min_dist = dist
                        target = (i, j)
    return target

#적 이동
def move_enemies(area):
    new_area = [[0] * m for _ in range(n)]
    for i in range(n - 1):
        for j in range(m):
            if area[i][j] == 1:
                new_area[i + 1][j] = 1
    return new_area


for l in archer_positions:
    area = [row[:] for row in arr]
    kill = 0
    while True:
        targets = set()

        for x,y in l:
            target = find_target(x,y,area)
            if target != (-1,-1):
                targets.add(target)
        for x,y in targets:
            if area[x][y] == 1:
                area[x][y] = 0
                kill +=1
        area = move_enemies(area)
        if sum(sum(row) for row in area) == 0:
            break
    answer = max(answer, kill)
print(answer)






