def solution(k, score):
    answer = []
    
    rank=[]
    for i in range(len(score)):
        if(i<k):
            rank.append(score[i])
            rank.sort()
            answer.append(rank[0])
        else:
            rank.append(score[i])
            rank.sort()
            rank.pop(0)
            answer.append(rank[0])
    
    return answer