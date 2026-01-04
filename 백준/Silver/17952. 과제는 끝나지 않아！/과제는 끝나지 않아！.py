import sys
input = sys.stdin.readline
n = int(input())
tmp = []
q = []
ans = 0
for _ in range(n):
    tmp = list(map(int, input().split()))

    if tmp[0] == 1:
        if tmp[2]-1 == 0:
            ans += tmp[1]
            continue
        q.append([tmp[1], tmp[2]-1])

    elif tmp[0] == 0:
        if len(q) > 0 :
            q[-1][1] -= 1
            if q[-1][1] <= 0 :
                ans += q[-1][0]
                q.pop()

print(ans)