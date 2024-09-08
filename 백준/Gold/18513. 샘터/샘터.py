import sys
input = sys.stdin.readline
from collections import deque


n,k = map(int, input().split())
sam = list(map(int, input().split()))

q = deque()
dict = {}

for s in sam:
    dict[s] = 0
    q.append(s)

def check(r):
    if r in dict.keys():
        return False
    return True

house =0
distence = 0
while q:
    cnt = q.popleft()
    rt = cnt+1
    lt = cnt-1

    if check(lt):
        house+=1
        dict[lt] = dict[cnt]+1
        distence += dict[lt]
        q.append(lt)
        if house >= k:
            print(distence)
            break


    if check(rt):
        house+=1
        dict[rt] = dict[cnt]+1
        distence += dict[rt]

        q.append(rt)
        if house >= k:
            print(distence)
            break