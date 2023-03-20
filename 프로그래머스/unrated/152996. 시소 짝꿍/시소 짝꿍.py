from collections import defaultdict
def solution(weights):
    answer = 0  
    
    siso = defaultdict(int)
    for weight in weights :
        siso[weight] += 1
        
    for key,value in siso.items():
        if value >1 :
            answer += value*(value-1)//2  #조합
        if key*2 in siso:
            answer += siso[key*2] * value
        if key*3%2 == 0 and key*3//2 in siso:
            answer += siso[key*3//2]*value
        if key*4%3 == 0 and key*4//3 in siso:
            answer += siso[key*4//3]*value
        

    return answer