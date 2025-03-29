def solution(s):
    answer = []
    
    if len(s) == 1:
        return 1
    
    idx = 1
    for i in range(1,len(s)//2+1):
        pre = s[:i]
        cnt = 1
        res = ''
        for j in range(i,len(s),i):
            if pre == s[j:j+i]:
                cnt+=1
            else:
                if cnt > 1:
                    res+= str(cnt) + pre
                else:
                    res += pre
                cnt = 1
                pre = s[j:j+i]
        if cnt>1:
            res += str(cnt) + pre
        else:
            res += pre
        answer.append(len(res))
        
        
                    
    
    return min(answer)