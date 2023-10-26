import math
def solution(begin, end):
    answer = []
    
    def find(n):
        if n == 1:
            return 0
        data = []
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                data.append(i)
                if n//i <=10000000:
                    return n//i
        if len(data)>=1:
            return data[-1]
        return 1
        
    for i in range(begin,end+1):
        answer.append(find(i))
    
    return answer