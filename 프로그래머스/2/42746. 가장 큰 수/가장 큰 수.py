def solution(numbers):
    answer = ''
    
    #앞자리수가 큰걸로 정렬
    #람다 사용
    
    numbers = sorted(map(str, numbers), key= lambda x:x*3,reverse=True)
    answer = ''.join(numbers)
    answer = '0' if answer[0]=='0' else answer
    return answer