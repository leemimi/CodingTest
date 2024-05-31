import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    q = []
    now = 0
    i = 0
    start = -1
    
    while i != len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(q,[j[1],j[0]])
        if q:
            cur = heapq.heappop(q)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i+=1
        else:
            now+=1
            
            
        
    
    
    return answer//len(jobs)