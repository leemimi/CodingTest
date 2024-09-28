def solution(order):
    answer = 0
    
    stack = []

    p = 0
    for i in range(1, len(order)+1):
        if i!= order[p]:
            stack.append(i)
        else:
            p+=1
            answer+=1
        while stack and order[p] == stack[-1]:
            stack.pop()
            p+=1
            answer+=1
        
    
    return answer