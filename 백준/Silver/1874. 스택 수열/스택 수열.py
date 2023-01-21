import sys
n = int(sys.stdin.readline())
s =1
flag = 0
stack =[]
answer =[]
for _ in range(n):
    num = int(input())
    while s<=num:
        stack.append(s)
        answer.append("+")
        s +=1
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag =1
        break
if flag == 0:
    for i in answer:
        print(i)