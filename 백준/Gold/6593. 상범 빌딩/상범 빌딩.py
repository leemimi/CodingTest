import sys
from collections import deque
input = sys.stdin.readline



dl = [1,-1,0,0,0,0]
dr = [0,0,1,-1,0,0]
dc = [0,0,0,0,1,-1]



def bfs():
    visited = [[[0]*C for _ in range(R)]for _ in range(L)]
    visited[sl][sr][sc] = 1
    q = deque([(sl,sr,sc)])

    while q:
        l,r,c = q.popleft()
        for i in range(6):
            nl = l +dl[i]
            nr = r + dr[i]
            nc = c + dc[i]

            if not (0<=nl<L and 0<=nr<R and 0<=nc<C):
                continue
            if visited[nl][nr][nc] or B[nl][nr][nc] == "#":
                continue
            if B[nl][nr][nc]=="E":
                print('Escaped in {} minute(s).'.format(visited[l][r][c]))
                return
            visited[nl][nr][nc] = visited[l][r][c]+1
            q.append((nl,nr,nc))
    print("Trapped!")


while True:
    L, R, C = map(int, input().split())
    if (L,R,C) == (0,0,0):
        break

    B = []
    sl,sr,sc = 0,0,0

    for l in range(L):
        B.append([list(input().rstrip()) for _ in range(R)])
        for r in range(R):
            for c in range(C):
                if B[l][r][c] == "S":
                    sl,sr,sc = l,r,c
        input()
    bfs()