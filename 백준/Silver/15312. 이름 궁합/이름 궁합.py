import sys
from collections import deque
input = sys.stdin.readline
alpha = [3,2,1,2,3,3,2,3,3,2,2,1,2,2,1,2,2,2,1,2,1,1,1,2,2,1]
a = input().strip()
b = input().strip()

q = deque()
for i in range(len(a)):
    q.append(alpha[ord(a[i]) - ord('A')])
    q.append(alpha[ord(b[i]) - ord('A')])

while len(q) > 2:
    temp = deque()
    prev = q.popleft()
    while q :
        cur = q.popleft()
        temp.append((prev+cur)%10)
        prev=cur
    q = temp

print(f"{q[0]}{q[1]}")