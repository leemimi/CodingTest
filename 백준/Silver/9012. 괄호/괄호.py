import sys
t = int(sys.stdin.readline())

for _ in range(t):
    stack = []
    s = input()

    for x in s:
        if x =='(':
            stack.append(x)
        if x ==')':
            if stack :
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")