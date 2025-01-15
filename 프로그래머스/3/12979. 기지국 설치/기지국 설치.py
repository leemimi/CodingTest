def solution(n, stations, w):
    answer = 0
    cover = w*2 +1
    start = 1
    for station in stations:
        lt, rt = station-w, station+w
    
        if start < lt:
            length = lt - start
            answer += (length+cover-1)//cover
            
        start = rt+1
        
    if start <= n:
        length = n-start +1
        answer += (length+cover-1)//cover
        
    
    

    return answer