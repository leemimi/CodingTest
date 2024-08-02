def solution(msg):
    answer = [0]
    # A:65
    dict={}
    for i in range(1,27):
        dict[chr(65+i-1)] = i
    
    w =''
    idx = 26
    for i in range(len(msg)):
        w += msg[i]
        if w not in dict:
            idx+=1
            dict[w] = idx
            w = msg[i]
            answer.append(dict[w])
            
        else:
            answer[-1] = dict[w]
            
    
            
    
    
    return answer