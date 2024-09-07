import sys
input = sys.stdin.readline

import heapq
N,T,P = map(int, input().split())
arr = []
for _ in range(T):
    inter, out = map(str,input().split())
    inter = int(inter[:2])*60+int(inter[2:])
    out = int(out[:2])*60+int(out[2:])
    arr.append((int(inter),int(out)))

arr.sort()
visited = [False]*(N+1)
ans = 720

def find_seat():
    maxdist = 0
    bs = 1
    for i in range(1,N+1):
        if visited[i]:
            continue

        lt = rt = float('inf')
        for j in range(i-1,0,-1):
            if visited[j]:
                lt = i-j
                break
        for j in range(i+1,N+1):
            if visited[j]:
                rt = j-i
                break
        dist = min(lt,rt)
        if dist>maxdist:
            maxdist=dist
            bs = i
        elif dist==maxdist and i < bs:
            bs = i
    return bs

q = []
for start,end in arr:
    while q and q[0][0] <=start:
        _, seat = heapq.heappop(q)
        visited[seat] = False

    best = find_seat()
    if best == P:
        ans -=(end-start)

    visited[best] = True
    heapq.heappush(q,(end, best))

print(ans)
