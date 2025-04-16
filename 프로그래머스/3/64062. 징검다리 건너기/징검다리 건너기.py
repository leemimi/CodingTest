from collections import deque
def solution(stones, k):
    answer = 0
    
    lt = 1
    rt = max(stones)+1
    
    while lt<rt-1:
        mid = (lt+rt)//2
        work = 0
        flag = True
        for stone in stones:
            if stone<mid:
                work +=1
            else:
                work = 0
            if work ==k:
                flag= False
                break
        if flag:
            lt = mid
        else:
            rt = mid
    
    
    return lt