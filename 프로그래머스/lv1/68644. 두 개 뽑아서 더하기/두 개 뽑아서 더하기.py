from itertools import combinations
def solution(numbers):
    answer = []
    
    def A(a,b):
        return a+b
    
    arr =[]
    arr= combinations(numbers,2)
    
    
    for a,b in arr:
        answer.append(A(a,b))
    
    answer = sorted(list(set(answer)))
    
    return answer