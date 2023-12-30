from collections import deque
def solution(priorities, location):
    ans = 0
    
    queue = [(i,v) for i,v in enumerate(priorities)]
    
    while True:
        x = queue.pop(0)
        if any(x[1] < q[1] for q in queue):
            queue.append(x)
        else:
            ans+=1
            if x[0] == location:
                return ans
    
    return ans