def solution(x):
    answer = True
    sum = 0;
    su = x
    while (x>0):
        sum += x%10
        x = x//10
    
    if(su%sum != 0):
        answer = False

    return answer