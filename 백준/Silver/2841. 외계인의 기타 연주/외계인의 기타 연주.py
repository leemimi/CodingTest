import sys
input = sys.stdin.readline

n, p = map(int, input().split())
cnt = 0

stack = [[] for _ in range(n)]
for _ in range(n):
    num, pret = map(int, input().split())
    num-=1

    now = stack[num]

    while now and now[-1] > pret:
        now.pop()
        cnt+=1

    if now and now[-1] == pret:
        continue
    now.append(pret)
    cnt+=1
print(cnt)
