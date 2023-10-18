import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dict = {}

for _ in range(n):
    dict[input().rstrip()] = 1

res = n
for _ in range(m):
    tmp = sorted(input().rstrip().split(','))

    for t in tmp:
        if t in dict.keys():
            if dict[t] == 1:
                dict[t] -=1
                res -=1
    print(res)