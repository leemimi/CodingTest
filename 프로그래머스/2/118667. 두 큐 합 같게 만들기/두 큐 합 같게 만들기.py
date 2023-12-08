from collections import deque
def solution(queue1, queue2):
    answer = 0
    limit = len(queue1)*4
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    asum = sum(q1) + sum(q2)
    
    if asum %2 != 0:
        return -1
    
    while True:
        if sum1> sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            answer +=1
        elif sum1 < sum2:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            answer+=1
        else:
            break
            
        if answer == limit:
            answer = -1
            break
        
    return answer