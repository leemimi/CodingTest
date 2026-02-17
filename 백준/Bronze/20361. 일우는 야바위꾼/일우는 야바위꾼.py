import sys
input = sys.stdin.readline
n, x, k = map(int, input().split())

now = x
for i in range(k):
    a,b = map(int, input().split())
    if now == a:
        now = b
    elif now == b:
        now = a
print(now)