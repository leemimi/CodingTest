from collections import deque
T = 10
for t in range(1, T + 1):
    tc = int(input())
    q = deque(list(map(int, input().split())))

    cnt = 1
    while True:
        a = q.popleft() - cnt
        if a <= 0 :
            q.append(0)
            break
        q.append(a)
        cnt += 1
        if cnt > 5 :
            cnt = 1

    arr = list(q)
    print(f"#{tc}", end=" ")
    print(*arr)
