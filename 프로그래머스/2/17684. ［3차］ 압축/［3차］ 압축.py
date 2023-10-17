def solution(msg):
    answer = []
    alp ={}
    for i in range(0,26):
        alp[chr(65+i)] = i+1
    
    
    k = 0
    while k < len(msg):
        wc = msg[k]
        i = 1
        while k+i < len(msg) and wc + msg[k+i] in alp:
            wc += msg[k+i]
            i += 1
        answer.append(alp[wc])
        if k+i < len(msg):
            alp[wc + msg[k+i]] = len(alp) + 1
        k += i
            
            
            
        
    return answer