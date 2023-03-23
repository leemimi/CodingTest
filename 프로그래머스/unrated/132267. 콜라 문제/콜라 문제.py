def solution(a, b, n):
    answer = 0
    

    while (n>=a):
        remain = n % a
        n = (n//a)*b
        answer+=n
        n+=remain
    
    return answer