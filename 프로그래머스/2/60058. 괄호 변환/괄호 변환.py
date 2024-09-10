def solution(p):
    answer = ''
    
    
    def vailed(a):
        stack = []
        for i in range(len(a)):
            if a[i] =='(':
                stack.append('(')
            else:
                if len(stack):
                    stack.pop()
                else:
                    return False
        return True
    
    
    def devide(c):
        lt, rt = 0,0
        for i in range(len(c)):
            if c[i] =='(':
                lt+=1
            else:
                rt+=1
            if lt == rt:
                return c[:i+1], c[i+1:]
    
    def solve(b):
        if not b:
            return ''
        
        u,v = devide(b)
        
        if vailed(u):
            return u + solve(v)
        else:
            tmp ='('
            s = solve(v)
            tmp+= s + ')'
            
            for s in u[1:len(u)-1]:
                if s=='(':
                    tmp+=')'
                else:
                    tmp+='('
        return tmp
            
    
        
    flag = True
    if vailed(p):
        return p
    else:
        answer = solve(p)
    
    
    return answer