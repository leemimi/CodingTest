def solution(name, yearning, photo):
    answer = []
    arr = {}
    for n, val in zip(name, yearning):
        arr[n] = val
    
        
    for ph in photo:
        cnt = 0
        for p in ph:
            if p in arr:
                cnt += arr[p]
        answer.append((cnt))
    return answer