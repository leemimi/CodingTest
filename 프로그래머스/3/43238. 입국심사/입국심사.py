def solution(n, times):
    answer = 0
    
    times.sort()
    
    lt = 1
    rt = max(times)*n
    while lt<=rt:
        mid = (lt+rt)//2
        
        p = 0
        
        for t in times:
            p += mid//t
            
            if p >=n:
                break
        if p >= n:
            answer = mid
            rt = mid -1
        elif p < n:
            lt = mid +1
            
            
    
    return answer