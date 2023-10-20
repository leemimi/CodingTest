from collections import deque
def solution(routes):
    answer = 1
    
    routes.sort(key = lambda x: x[1])
    prev = routes[0][1]
    
    for start, end in routes:
        if start > prev:
            answer +=1
            prev = end
            
    
    return answer


