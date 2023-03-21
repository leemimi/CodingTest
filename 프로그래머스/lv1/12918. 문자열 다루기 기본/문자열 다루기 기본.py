def solution(s):
    answer = False
    if(s.isdigit()):
        if(len(s)==4 or len(s)==6):
            answer= True
    return answer