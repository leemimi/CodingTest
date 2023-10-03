from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    
    arr = defaultdict(int)
    for d in tangerine:
        arr[d] +=1
    
    arr = dict(sorted(arr.items(), key=lambda x:x[1], reverse=True))
    
    for i in arr:
        if k<=0:
            return answer
        k-=arr[i]
        answer+=1
        
    
    return answer