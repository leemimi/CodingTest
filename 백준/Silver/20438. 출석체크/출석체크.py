import sys

n, k, q, m = map(int, sys.stdin.readline().split())
k_arr = set(list(map(int, input().split())))
q_arr = set(list(map(int, input().split())))
find = []
for _ in range(m):
    s,e = map(int, input().split())
    find.append((s,e))
nums = [i for i in range(3,n+3)]
dp = [0]*(n+3)
for q in (q_arr - k_arr):
    for i in range(q, n+3, q):
        if i not in k_arr:
            dp[i] = 1

attend = [0]*(n+3)
for i in range(3,n+3):
    if not dp[i]:
        attend[i] = attend[i-1] +1
    else:
        attend[i] = attend[i-1]
answer=[]
for s,e in find:
    answer.append(attend[e]- attend[s-1])

for a in answer:
    print(a)