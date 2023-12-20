def solution(number, k):
    answer = ''
    stack = []
    t = len(number) - k
    for n in number:
        if len(stack) < 1:
            stack.append(n)
            continue
        while stack[-1] < n and k>0:
            stack.pop()
            k-=1
            if not stack or k <= 0:
                break
        stack.append(n)
        if len(stack) == len(number) - k:
            break
    
    return ''.join(stack)

