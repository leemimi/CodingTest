from collections import defaultdict
from operator import itemgetter
def solution(strings, n):
    answer = []
    
    strings.sort()
    arr = defaultdict(str)
    for i in range(len(strings)):
        arr[i]+=strings[i][n]
        
    sort_value = sorted(arr.items(), key=itemgetter(1))
    
    
    
    for idx in sort_value:
        answer.append(strings[idx[0]])
        
    return answer