import sys
input = sys.stdin.readline
from collections import deque
n,k = map(int, input().split())
sam = list(map(int, input().split()))

dict = {}
q = deque()

for s in sam:
    dict[s] = 0
    q.append(s)

def check(now):
    if now in dict.keys():
        return False
    return True

house = 0
total = 0
while q:
    cnt = q.popleft()
    rc = cnt+1
    lc =cnt-1
    if check(rc):
        dict[rc] = dict[cnt]+1
        house +=1
        total += dict[rc]
        if house>=k:
            print(total)
            exit()
        q.append(rc)
    if check(lc):
        dict[lc] = dict[cnt]+1
        house+=1
        total += dict[lc]
        if house>=k:
            print(total)
            exit()
        q.append(lc)