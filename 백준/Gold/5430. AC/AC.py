import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    num = int(input())
    arr = input().rstrip()[1:-1].split(",")


    if "" in arr:
        arr.pop()
    flag = True
    reverse_stat = 0
    arr = deque(arr)
    for s in p:
        if s == 'R':
            reverse_stat +=1
        elif s == 'D':
            if len(arr) ==0:
                flag =False
                break
            elif reverse_stat % 2 ==0:
                arr.popleft()
            else:
                arr.pop()
    if flag:
        if reverse_stat%2!=0:
            arr.reverse()
        print("[",end="")
        print(",".join(arr),end="")
        print("]")
    else:
        print("error")