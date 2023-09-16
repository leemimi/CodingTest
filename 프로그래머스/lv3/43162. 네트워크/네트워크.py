def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a,b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    
    parent = [i for i in range(n+1)]
    
    for i in range(n):
        for j in range(n):
            if i == j : continue
            if computers[i][j] == 1:
                union(parent, i+1, j+1)
    maps = {}
    for idx in range(1, len(parent)):
        v = find(parent, parent[idx])
        if not v in maps:
            maps[v] = 1
            
    return len(maps)