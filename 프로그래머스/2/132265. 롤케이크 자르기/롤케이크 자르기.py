from collections import Counter
def solution(topping):
    answer = 0
    
    old = Counter(topping)
    young = set()
    
    for t in topping:
        old[t] -=1
        young.add(t)
        
        if old[t] == 0:
            old.pop(t)
        if len(old.keys()) == len(young):
            answer+=1
    
    
    
    return answer