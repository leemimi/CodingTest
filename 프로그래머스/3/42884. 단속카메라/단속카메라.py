def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x:(x[1],x[0]))
    stack =[]
    for route in routes:
        if not stack:
            stack.append(route)
        if stack[-1][1] >= route[0]:
            continue
        else:
            stack.append(route)
    
        
    
    print(stack)
    return len(stack)