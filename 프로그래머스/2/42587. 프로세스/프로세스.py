from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque(enumerate(priorities))
    while q:
        idx,p = q.popleft()
        
        if any( pp > p for _,pp in q):
            q.append((idx,p))
        else:
            answer+=1
            if(idx == location):
                return answer
        
        
    
    return answer