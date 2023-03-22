from itertools import combinations
def solution(number):
    answer = 0
    
    number.sort()
    arr =[]
    arr = list(combinations(number,3))
    

    for i in range(len(arr)):
            if sum(arr[i]) == 0:
                answer+=1

                
    return answer