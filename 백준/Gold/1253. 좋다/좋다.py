import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0

for i in range(n):
    goal = arr[i]
    lt = 0
    rt = n-1
    while lt<rt:
        res = arr[lt] + arr[rt]
        if res == goal:
            if lt == i:
                lt+=1
            elif rt == i:
                rt -= 1
            else:
                cnt+=1
                break
        elif res > goal:
            rt -=1
        else:
            lt+=1

print(cnt)