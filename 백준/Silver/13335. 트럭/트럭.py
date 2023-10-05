from collections import deque

n,w,l = map(int, input().split())
arr = list(map(int, input().split()))

truck = deque(arr)
bridge = deque([0]*w)

cnt = 0
while truck:
    bridge.popleft()
    t=truck[0]
    if len(bridge) < w and sum(bridge) + t <=l:
        bridge.append(truck.popleft())
    else:
        bridge.append(0)
    cnt+=1


print(cnt+w)

