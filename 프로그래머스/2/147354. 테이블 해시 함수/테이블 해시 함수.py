def solution(data, col, row_begin, row_end):
    answer = 0
    
    data = sorted(data, key = lambda x:[x[col-1],-x[0]])
    arr = []
    for i in range(row_begin-1, row_end):
        cnt = 0
        for j in data[i]:
            cnt += j%(i+1)
        arr.append(cnt)
    
    answer = arr[0]
    for i in range(1,len(arr)):
        answer ^= arr[i]
    
        
    return answer