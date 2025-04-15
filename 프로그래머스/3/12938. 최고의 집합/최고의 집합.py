def solution(n, s):
    answer = []
    
    if s//n==0:
        return [-1]
    
    for _ in range(n-s%n):
        answer.append(s//n)
        
    for _ in range(s%n):
        answer.append(s//n+1)

    
    return answer
