def solution(n, times):
    answer = 0
    lt,rt = 0, times[-1]*n
    
    while lt <= rt:
        mid = (rt+lt)//2
        res = 0
        for i in range(len(times)):
            res += mid//times[i]
            if res >=n:
                break
        if res >= n:
            answer = mid
            rt = mid -1
        else:
            lt = mid + 1
        
    
    return answer