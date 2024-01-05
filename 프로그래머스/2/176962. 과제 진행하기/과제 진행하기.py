def solution(plans):
    answer = []
    
    def times(t):
        a,b=t.split(':')
        return int(a)*60 + int(b)
    
    for p in plans:
        p[1] = times(p[1])
        p[2] = int(p[2])
    plans.sort(key=lambda x:x[1])
    
    stack = []
    for i in range(len(plans)):
        if i == len(plans)-1:
            stack.append(plans[i])
            break
        
        lan, st, t = plans[i]
        nlan, nst, nt = plans[i+1]
        
        if st + t <= nst:
            answer.append(lan)
            tmp_time = nst - (st+t)
            
            while tmp_time != 0 and stack:
                tsub, tst, tt = stack.pop()
                if tmp_time >= tt:
                    answer.append(tsub)
                    tmp_time -= tt
                else:
                    stack.append([tsub,tst,tt- tmp_time])
                    tmp_time = 0
        else:
            plans[i][2] = t-(nst-st)
            stack.append(plans[i])
            
    while stack:
        sub,st,tt = stack.pop()
        answer.append(sub)
        
        
    
    return answer