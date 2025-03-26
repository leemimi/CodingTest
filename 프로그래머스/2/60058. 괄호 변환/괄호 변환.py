def devide(n):
    lt = 0
    rt = 0
    for i in range(len(n)):
        if n[i] == '(':
            lt+=1
        else:
            rt+=1
        if lt == rt:
            return n[:i+1], n[i+1:]
def check(s):
    stack = []
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True
    
def solution(p):
    answer = ''
    # 1번
    if not p:
        return ''
    
    #2번수행 나누자
    u, v = devide(p)
    
    #3번 문자열 u 검증
    flag = check(u)
    if flag:
        return u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        u = u[1:len(u)-1]
        for i in u:
            if i =='(':
                answer += ')'
            else:
                answer+= '('
        return answer
            

        
            
        
    if len(stack) == 0:
        return p
            
    
    return answer