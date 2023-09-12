from collections import deque


def right_side(idx, dir):
    global arr
    if idx > 2 :
        return
    elif arr[idx][2] != arr[idx+1][6]:
        right_side(idx + 1, -dir)
        arr[idx+1].rotate(dir)

def left_side(idx, dir):
    global arr
    if idx < 1 :
        return
    elif arr[idx][6] != arr[idx-1][2]:
        left_side(idx - 1, -dir)
        arr[idx-1].rotate(dir)


arr = []
for _ in range(4):
    arr.append(deque(input()))
k= int(input())

cnt = 0
for _ in range(k):
    num, dir = map(int, input().split())

    right_side(num-1, -dir)
    left_side(num-1, -dir)
    arr[num-1].rotate(dir)


if arr[0][0] == '1' :
    cnt+=1
if arr[1][0] == '1' :
    cnt+=2
if arr[2][0] == '1' :
    cnt+=4
if arr[3][0] == '1' :
    cnt+=8

print(cnt)