def solution(name, yearning, photo):
    answer = []
    
    yName = list(zip(name,yearning))
    
    
    for i in range(len(photo)):
        score = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                idx=name.index(photo[i][j])
                score+=yearning[idx]
        answer.append(score)
        score=0

    
        
    
    return answer