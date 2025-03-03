def solution(info, n, m):
    answer = 0
    dp = {(0,0)}
    
    
    for acost,bcost in info:
        new_dp = set()
        for a, b in dp:
            if a+acost < n:
                new_dp.add((a+acost, b))
            if b+bcost < m:
                new_dp.add((a, b+bcost))
        
        dp = new_dp
        if not dp:
            return -1
    
    return min(a for a,b in dp)