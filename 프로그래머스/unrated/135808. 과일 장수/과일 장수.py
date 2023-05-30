def solution(k, m, score):
    answer = 0
        
    score.sort(reverse=True)

    for i in range(m-1,len(score),m):
        apple = 0
        answer+= score[i]*m

        

    
    return answer