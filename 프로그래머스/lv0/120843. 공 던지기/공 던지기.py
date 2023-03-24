
def solution(numbers, k):
    answer = 0
    
    i=0
    while (k>0):
        answer = numbers[i%len(numbers)]
        i+=2
        k-=1
    
    return answer