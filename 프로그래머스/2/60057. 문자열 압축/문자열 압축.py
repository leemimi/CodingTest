def solution(s):
    answer = len(s)
    for x in range(1,len(s)//2+1):
        cnt = 1
        prev = ''
        prev_len = 0
        for i in range(0,len(s)+1,x):
            tmp = s[i:i+x]
            if prev == tmp:
                cnt+=1
            elif prev!=tmp:
                prev_len += len(tmp)
                if cnt>1:
                    prev_len += len(str(cnt))
                cnt = 1
                prev = tmp
        answer = min(answer, prev_len)
        
    
    
    return answer