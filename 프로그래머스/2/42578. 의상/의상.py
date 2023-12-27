def solution(clothes):
    answer = 1
    dict = {}
    for name, id in clothes:
        if id not in dict:
            dict[id] =[name]
        else:
            dict[id].append(name)
    

    for v in dict.values():
        answer = (len(v)+1)*answer
    
    
    
    return answer-1