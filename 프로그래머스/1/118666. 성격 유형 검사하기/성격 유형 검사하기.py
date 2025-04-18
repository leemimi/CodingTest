from collections import defaultdict
def solution(survey, choices):
    answer = ''
    mbti = {
        'R':0, 'T':0, 'C':0, 'F':0,'J':0,'M':0,'A':0,'N':0
    }
    
    for s,c in zip(survey, choices):
        if c<4 : mbti[s[0]] += 4-c
        elif c>4 : mbti[s[1]] += c-4 
    
    mbti = list(mbti.items())
    
    for i in range(0,8,2):
        if mbti[i][1] >= mbti[i+1][1]:
            answer+=mbti[i][0]
        else:
            answer+=mbti[i+1][0]
            
    return answer
