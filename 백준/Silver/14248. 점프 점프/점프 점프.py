from collections import deque

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

s = s-1

q = deque()

q.append(s)
cnt = 0
visited = [0]*n
while q:
    now = q.popleft()

    visited[now] = 1

    nx = now + arr[now]
    ny = now -arr[now]

    if 0<=nx<n and not visited[nx]:
        visited[nx] = 1
        q.append(nx)
        cnt+=1
    if 0<=ny<n and not visited[ny]:
        visited[ny] = 1
        q.append(ny)
        cnt+=1

print(cnt+1)
