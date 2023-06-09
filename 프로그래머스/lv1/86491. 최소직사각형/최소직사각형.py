def solution(sizes):
    answer = 0
    w = []
    h = []
    for s in sizes:
        w.append(max(s[0],s[1]))
        h.append(min(s[0],s[1]))
        
    answer = max(w)*max(h)
    
            
    return answer