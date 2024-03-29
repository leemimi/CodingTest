from collections import deque
def solution(people, limit):
    answer = 0
    
    people.sort()
    dq = deque(people)
    
    while len(dq)>1 :
        if dq[0] + dq[-1] <=limit:
            dq.popleft()
        answer+=1    
        dq.pop()
    if dq :
        answer+=1
    return answer