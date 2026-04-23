def solution(n):
    answer = ''
    a = '수'
    b = '박'
    
    for i in range(n):
        if i%2 == 0:
            answer += '수'
        else:
            answer += '박'
    
    return answer