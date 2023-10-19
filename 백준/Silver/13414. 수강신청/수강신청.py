import sys
input = sys.stdin.readline
from collections import defaultdict

l,k = map(int, input().split())
dict = defaultdict(int)
for _ in range(k):
    p = input().rstrip()
    if p not in dict:
        dict[p] = 1
    if p in dict:
        del dict[p]
        dict[p] = 1

cnt = 0
for k in dict:
    print(k)
    cnt +=1
    if cnt == l:
        break