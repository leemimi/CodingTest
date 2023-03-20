def solution(cards1, cards2, goal):
    
    for s in goal:
        if len(cards1) and s == cards1[0] :
            cards1.pop(0)
        elif len(cards2) and  s ==cards2[0] :
            cards2.pop(0)
        else:
            return 'No'
    
    return 'Yes'
