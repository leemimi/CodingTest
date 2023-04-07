def solution(babbling):
    answer = 0
    
    words = ["aya","ye","woo","ma"]
    
    for ba in babbling:
        for w in words:
            if w*2 not in ba:
                ba = ba.replace(w,' ')
        if len(ba.strip())==0:
            print("ba =", ba)
            answer+=1
    
    return answer