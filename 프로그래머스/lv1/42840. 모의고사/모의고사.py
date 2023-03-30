def solution(answers):
    answer = []
    
    people1=[1,2,3,4,5]*len(answers)
    people2=[2,1,2,3,2,4,2,5]*len(answers)
    people3=[3,3,1,1,2,2,4,4,5,5]*len(answers)
    
    score=[0,0,0]
    for i in range(len(answers)):
        if(answers[i] == people1[i]):
            score[0]+=1
        if(answers[i] == people2[i]):
            score[1]+=1
        if(answers[i] == people3[i]):
            score[2]+=1
        
    for i,v in enumerate(score):
        if(v == max(score)):
            answer.append(i+1)
        
    
    
    
    
    return answer