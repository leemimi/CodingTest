def solution(s):
    answer = True
    a=s.upper()
    
    if a.count('P') != a.count('Y'):
        answer =False
    else:
        answer =True
    if a.count('P') == 0 and a.count('Y')==0:
        answer = True

    return answer