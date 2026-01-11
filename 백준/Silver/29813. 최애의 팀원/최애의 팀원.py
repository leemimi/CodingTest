import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
lst = deque()
for _ in range(n):
    a,b = map(str, input().split())
    lst.append([a,b])
while len(lst) > 2:
    i, cnt = lst.popleft()
    cnt = int(cnt)

    while True:
        cnt -=1
        if cnt == 0:
            c, d = lst.popleft()
            break
        c,d = lst.popleft()
        lst.append([c,d])

print(lst[0][0])