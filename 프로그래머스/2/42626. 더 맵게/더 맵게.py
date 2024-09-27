import heapq
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    
    while len(scoville)>1:
        t = heapq.heappop(scoville)
        if t >=K:
            break
        tmp = t + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville,tmp)
        answer +=1
        
    
    if scoville[0] < K:
        return -1
        
    
        
    return answer