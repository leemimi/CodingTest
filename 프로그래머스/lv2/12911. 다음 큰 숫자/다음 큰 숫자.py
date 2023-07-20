def solution(n):
    answer = n
    onecnt = bin(n).count('1')
    while True:
        answer +=1
        answercnt = bin(answer).count('1')
        if answercnt == onecnt:
            break
    
    
    return answer