def solution(sequence, k):
    answer = [0, len(sequence)]
    n = len(sequence)
    
    sums = sequence[0]
    lt =0
    rt = 0
    
    while True:
        if sums < k:
            rt+=1
            if rt == n:
                break
            sums+= sequence[rt]

        else:
            if sums == k:
                if answer[1]-answer[0] > rt -lt:
                    answer = [lt, rt]
            sums-= sequence[lt]
            lt+=1



    return answer