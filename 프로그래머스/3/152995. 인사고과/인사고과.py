def solution(scores):
    answer = 0
    wanho = scores[0]
    wsum = sum(scores[0])
    
    scores.sort(key = lambda x: (-x[0],x[1]))
    
    t = 1
    now = 0
    for s in scores:
        if wanho[0] < s[0] and wanho[1] <s[1]:
            return -1
    
        if now <= s[1]:
            if wsum < s[0]+s[1]:
                t+=1
            now= s[1]

    
    return t