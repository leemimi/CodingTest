def solution(k, ranges):
    answer = []
    
    #우박수열 계산
    arr =[]
    while (k!=1):
        arr.append(k)
        if k%2==0:
            k = k/2
        else:
            k = k*3 +1
    arr.append(k) 

    
    for x1,x2 in ranges:
        sums = 0
        ub = arr[x1:len(arr)+x2]
        if x1>=x2+len(arr):
            answer.append(-1)
            continue
           
        for i in range(len(ub)-1):
            sums+=((ub[i]+ub[i+1])*1)/2
        answer.append(sums)
            
        
        

            
    
    return answer