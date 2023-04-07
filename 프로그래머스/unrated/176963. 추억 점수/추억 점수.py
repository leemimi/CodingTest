def solution(name, yearning, photo):
    answer = []
    
    yName = list(zip(name,yearning))
    
    s = 0
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                idx=name.index(photo[i][j])
                s+=yearning[idx]
        answer.append(s)
        s=0

    
        
    
    return answer