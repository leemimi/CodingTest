def solution(s):
    answer = 0
    
    
    for _ in range(len(s)):
        stack = []
        for k in s:
            if len(stack) == 0:
                stack.append(k)
            else:
                if k == ']' and stack[-1] == '[':
                    stack.pop()
                elif k == '}' and stack[-1] == '{':
                    stack.pop()
                elif k == ')' and stack[-1] == '(':
                    stack.pop()
                else: stack.append(k)
        if len(stack)==0:
            answer+=1
        tmp = s[0]
        s=s[1:]+tmp
                 
        
    return answer