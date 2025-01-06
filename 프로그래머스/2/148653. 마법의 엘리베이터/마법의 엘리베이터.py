def solution(storey):
    answer = 0
    
    while storey:
        storey, r = storey//10, storey%10
        
        if r<5 or (r==5 and storey%10<5):
            answer += r

        else:
            answer += (10 -r )
            storey+=1
    
    return answer