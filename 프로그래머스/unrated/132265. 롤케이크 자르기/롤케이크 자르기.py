from collections import Counter
def solution(topping):
    answer = 0
    
    a = set()
    dic = Counter(topping)
    for t in topping:
        dic[t] -=1
        a.add(t)
        if dic[t] == 0:
            dic.pop(t)
        if len(dic) == len(a):
            answer+=1
            
        
    return answer