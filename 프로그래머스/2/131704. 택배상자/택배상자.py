from collections import deque
def solution(order):
    answer = 0
    stack = []
    idx = 0
    now = 0
    
    while idx<len(order):
        if order[idx] > now:
            now+=1
            stack.append(now)
        elif order[idx] == stack[-1]:
            stack.pop()
            idx+=1
        else:
            return idx

    
    
    
    return idx