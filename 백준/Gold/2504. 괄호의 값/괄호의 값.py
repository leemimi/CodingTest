s = input()
stack = []
tmp = 1
answer = 0
for i in range(len(s)):
    if s[i] =='(':
        tmp *= 2
        stack.append(('('))
    elif s[i] == '[':
        tmp *= 3
        stack.append(('['))
    elif s[i] ==')':
        if not stack or stack[-1] =='[':
            answer = 0
            break
        if s[i-1] =='(':
            answer +=tmp
        stack.pop()
        tmp //=2
    else:
        if not stack or stack[-1] =='(':
            answer= 0
            break
        if s[i-1] =='[':
            answer+=tmp
        stack.pop()
        tmp//=3

if stack:
    print(0)
else:
    print(answer)