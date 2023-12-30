from collections import Counter
def solution(progresses, speeds):
    answer = []
    
    res = []
    for i in range(len(progresses)):
        tmp = (100 - progresses[i])//speeds[i]
        if (100 - progresses[i])%speeds[i] > 0:
            tmp+=1
    
        if len(res) < 1:
            res.append(tmp)
        elif len(res) >= 1 and res[-1] >= tmp:
            res.append(res[-1])
        elif len(res) >= 1 and res[-1] < tmp:
            res.append(tmp)
    
    l = Counter(res)
    for k,v in l.items():
        answer.append(v)
    
    return answer