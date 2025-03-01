from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    if (sum1+sum2)%2!=0:
        return -1
    while(sum1!= sum2):
        if answer > 600000:
            return -1
        if sum1 > sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        elif sum2 > sum1:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
        else:
            return answer
        answer+=1
    
    return answer