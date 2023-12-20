def solution(sequence, k):
    answer = [0,len(sequence)]
    
    lt = 0
    rt = 0
    
    res = sequence[0]
    
    while True:
        if res<k:
            rt+=1
            if rt == len(sequence):break
            res+=sequence[rt]
        else:
            if res == k:
                if rt - lt < answer[1] - answer[0]:
                    answer = [lt,rt]
            res -= sequence[lt]
            lt+=1
    
    return answer