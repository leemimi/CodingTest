def solution(topping):
    answer = 0
    
    lt = set()
    rt = {}
    
    for t in topping:
        if t in rt:
            rt[t] +=1
        else:
            rt[t] = 1
            
    for t in topping:
        lt.add(t)
        rt[t] -=1
        if rt[t] == 0:
            del rt[t]
        if len(lt) == len(rt):
            answer+=1
    
    
    return answer