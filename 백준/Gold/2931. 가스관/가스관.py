import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
opp = [1, 0, 3, 2]

conn = {
    '|': [0, 1],
    '-': [2, 3],
    '+': [0, 1, 2, 3],
    '1': [1, 3],
    '2': [0, 3],
    '3': [0, 2],
    '4': [1, 2]
}


for i in range(R):
    for j in range(C):
        if arr[i][j] != '.':
            continue

        q = []
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if 0<= ni <R and 0<= nj < C:
                if arr[ni][nj] != '.' and opp[d] in conn.get(arr[ni][nj], []):
                    q.append(d)
        if len(q) < 2: 
            continue
        
        q = sorted(q)
        
        if q == [0, 1, 2, 3]:
            block = '+'
        elif q == [0, 1]:
            block = '|'
        elif q == [2, 3]:
            block = '-'
        elif q == [1, 3]:
            block = '1'
        elif q == [0, 3]:
            block = '2'
        elif q == [0, 2]:
            block = '3'
        elif q == [1, 2]:
            block = '4'
        else:
            continue

        print(i + 1, j + 1, block)
        exit()