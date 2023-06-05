def solution(lottos, win_nums):
    answer =[]
    
    match = 0
    
    for num in lottos:
        if num in win_nums:
            match +=1
    cnts = []
    cnts.append(match)
    cnts.append(match+lottos.count(0))
    for match in cnts:
        print(match)
        if match <= 1 :
            answer.append(6)
        elif match ==2:
            answer.append(5)
        elif match ==3:
            answer.append(4)
        elif match == 4:
            answer.append(3)
        elif match == 5 :
            answer.append(2)
        elif match == 6 :
            answer.append(1)
        print(answer)
        
        
    return answer[::-1]