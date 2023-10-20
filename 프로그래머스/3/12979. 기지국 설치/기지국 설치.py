import math
def solution(n, stations, w):
    answer = 0
    W = 2*w+1
    start = 1
    for s in stations:
        
        answer += max(math.ceil((s-w-start)/W),0)
        start = s+w+1
        
    if n>= start:
        answer += math.ceil((n-start+1)/W)
        

    return answer