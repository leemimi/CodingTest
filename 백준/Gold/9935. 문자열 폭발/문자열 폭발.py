s = input()
t = list(input())

stack = []
want = len(t)

for c in s:
    stack += c
    if len(stack)>=want and stack[-want:] == t:
        del (stack[-want:])

if len(stack) < 1:
    print("FRULA")
else:
    res = ''.join(stack)
    print(res)