import copy
import sys
from itertools import combinations

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def solve():
    global res
    for wall in combinations(safe, 3):
        test = copy.deepcopy(arr)
        for a,b in wall:
            test[a][b] = 1
        queue = list(virus)
        while queue:
            x,y = queue.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y +dy[i]
                if 0<=nx<n and 0<=ny<m and test[nx][ny] == 0:
                    test[nx][ny] = 2
                    queue.append((nx,ny))

        cnt = sum(row.count(0) for row in test)
        res = max(res, cnt)


n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

safe = [(i, j) for i in range(n) for j in range(m) if arr[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if arr[i][j] == 2]

res = 0
solve()
print(res)
