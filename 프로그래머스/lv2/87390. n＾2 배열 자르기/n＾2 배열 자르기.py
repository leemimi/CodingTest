def solution(n, left, right):
    answer = []
    
    
    for i in range(left, right+1):
        x = i//n
        y = i%n
        
        if x<=y :
            x,y = y,x
        answer.append(x+1)

    return answer