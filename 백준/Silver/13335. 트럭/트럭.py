from collections import deque

n,w,l = map(int, input().split())
arr = list(map(int, input().split()))

truck = deque(arr)
b = deque([0]*w)
time = 0
while truck:
    b.popleft()
    t = truck[0]
    if len(b) < w and sum(b)+t <= l:
        b.append(truck.popleft())
    else:
        b.append(0)
    time+=1

print(time+w)