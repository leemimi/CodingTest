def solution(msg):
    answer = []
    dict = {chr(idx + 64):idx for idx in range(1, 27)}
    key = 27
    
    w = c= 0
    while True:
        c+=1
        if c ==len(msg):
            answer.append((dict[msg[w:c]]))
            break
            
        if msg[w:c+1] not in dict:
            dict[msg[w:c+1]] = key
            key+=1
            answer.append(dict[msg[w:c]])
            w=c
            
    
    return answer