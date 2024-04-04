def solution(n, s):
    answer = []
    
    if s//n <= 0 : return [-1]
    
    for i in range(n):
        answer.append(s//n)
    
    for i in range(s%n):
        answer[i] += 1
    
    answer.sort()
    
    return answer