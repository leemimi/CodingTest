import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
crain = list(map(int, input().split()))
bb = int(input())
boxes = list(map(int, input().split()))

crain.sort(reverse=True)
boxes.sort(reverse=True)

time = 0
if boxes[0] > crain[0]:
    time=-1
else:
    while boxes:
        for i in range(n):
            if boxes and crain[i] < boxes[-1]:
                continue
            for b in boxes:
                if crain[i] >= b:
                    boxes.remove(b)
                    break
        time+=1

print(time)