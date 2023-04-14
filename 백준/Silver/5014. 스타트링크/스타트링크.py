import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue=deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        if v == G:
            return count[G]
        for i in (v+U, v-D):
            if 0< i <=F and not visited[i]:
                visited[i] =1
                count[i] = count[v]+1
                queue.append(i)
    if count[G] == 0:
        return "use the stairs"

F, S, G, U, D = map(int, input().split())
visited =[0 for i in range(F+1)]
count = [0 for i in range(F+1)]

print(bfs(S))