def solution(ingredient):
    answer = 0
    i = 0
    while i <= len(ingredient)-2:
        if ingredient[i:i+4] == [1,2,3,1]:
            del(ingredient[i:i+4])
            i = i-3
            answer+=1
        i+=1
            
    
    return answer