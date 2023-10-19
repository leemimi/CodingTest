def solution(n, times):
    answer = 0
    
    lt = 1
    rt = max(times)*n
    
    while lt<=rt:
        mid = (lt+rt)//2
        people = 0
        for time in times:
            people += mid//time
            if people >= n:
                break
        if people >= n:
            answer = mid
            rt = mid-1
        else:
            lt = mid +1
        
    return answer