from collections import deque
def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return arr[v]
        for next in (v-1, v+1, 2*v):
            if 0<= next< MAX and not arr[next]:
                arr[next] = arr[v]+1
                q.append(next)

n,k = map(int, input().split())
MAX = 100001
arr = [0]*MAX
print(bfs(n))