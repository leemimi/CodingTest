import sys
from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dq = deque(list(map(int, sys.stdin.readline().split())))
    idx = deque(list(range(n)))
    cnt=0

    while dq:
        large = max(dq)
        if large == dq[0]:
            dq.popleft()
            px =idx.popleft()
            cnt +=1

            if px == m:
                break

        else :
            cur = dq.popleft()
            dq.append(cur)
            a = idx.popleft()
            idx.append(a)


    print(cnt)