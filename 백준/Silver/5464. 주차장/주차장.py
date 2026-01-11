import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int, input().split())
park = []
car = []
lst = []

for _ in range(n):
    park.append(int(input().strip()))
for _ in range(m):
    car.append(int(input().strip()))

q = deque()
parking = [0]*n
ans = 0
for i in range(m*2):
    c = int(input().strip())

    if c>0:
        if 0 in parking:
            for j in range(n):
                if parking[j] == 0:
                    parking[j] = c
                    break
        else:
            q.append(c)
    else:
        a = parking.index(-c)
        parking[a] = 0
        ans += car[-c-1]*park[a]
        if q:
            parking[a] = q.popleft()
print(ans)