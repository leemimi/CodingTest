def solution(plans):
    answer = []
    
    for i in range(len(plans)):
        s= plans[i][1].split(':')
        plans[i][1] = int(s[0])*60+int(s[1])
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key= lambda x:x[1])
    stack = []
    stack.append(plans[0])
    
    now = plans[0][1]
    for i in range(1, len(plans)):
        lang, start, spend = plans[i]
        while stack:
            sl, ss, sp = stack.pop()

            if now <= ss:
                now = ss
            
            finish = now + sp
            
            if finish <= start:
                answer.append(sl)
                now += sp
            else:
                stack.append([sl, ss, finish - start])
                now = start
                break
        stack.append(plans[i])

    while stack:
        l = stack.pop()[0]
        answer.append(l)

    return answer