import sys
k = int(sys.stdin.readline())

stack =[]
for _ in range(k):
    su = int(sys.stdin.readline())
    if su ==0:
        stack.pop()
    if su !=0:
        stack.append(su)

print(sum(stack))