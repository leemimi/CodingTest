def solution(a):
    answer = 0
    
    res = [False]*len(a)
    minf = float('inf')
    minb = float('inf')
    
    for i in range(len(a)):
        if a[i] < minf:
            minf = a[i]
            res[i] = True
        if a[-1-i] < minb:
            minb = a[-1-i]
            res[-1-i] = True
        
    
    return sum(res)