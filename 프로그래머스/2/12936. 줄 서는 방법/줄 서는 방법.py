import math
def solution(n, k):
    answer = [i for i in range(1,n+1)]
    k = k-1
    stack = []
    while answer:
        a = k//math.factorial(n-1)
        stack.append(answer[a])
        del answer[a]
        
        k = k%math.factorial(n-1)
        n -=1
    
    return stack