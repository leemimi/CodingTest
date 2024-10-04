from collections import defaultdict
def solution(gems):
    answer = [0, len(gems)-1]
    
    dict = defaultdict(int)
    gem = set(gems)
    
    lt = 0
    rt = 0
    
    n = len(gems)
    mins = len(gems)+1
    while rt<n:
        
        dict[gems[rt]]+=1
        
        
        while len(gem) == len(dict):
            if rt-lt < mins:
                mins = rt - lt
                answer = [lt, rt]
            
            dict[gems[lt]]-=1
            if dict[gems[lt]] == 0:
                del dict[gems[lt]]
            lt+=1
        rt+=1
    
    return [answer[0]+1, answer[1]+1]