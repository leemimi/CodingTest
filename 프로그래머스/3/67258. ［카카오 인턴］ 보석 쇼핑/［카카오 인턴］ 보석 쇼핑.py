from collections import defaultdict
def solution(gems):
    answer = [0,len(gems)-1]
    gem = set(gems)
    lt = 0
    rt = 0
    
    dict = defaultdict(int)
    min = len(gems)+1
    n = len(gems)
    while rt<n:
        dict[gems[rt]] +=1

        while len(gem) == len(dict):
            if rt-lt < min:
                answer = [lt,rt]
                min = rt -lt
            dict[gems[lt]]-=1
            if dict[gems[lt]] == 0:
                del dict[gems[lt]]
            lt+=1
        rt+=1
            
    
    return [answer[0]+1, answer[1]+1]