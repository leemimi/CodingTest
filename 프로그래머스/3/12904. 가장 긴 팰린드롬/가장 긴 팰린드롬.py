def solution(s):
    answer = 0
    
    def find1(lt,rt):
        while lt>=0 and rt<len(s) and s[lt] == s[rt]:
            lt-=1
            rt+=1
        return rt-lt-1
    
    def find2(lt,rt):
        while lt>=0 and rt<len(s) and s[lt] == s[rt]:
            lt-=1
            rt+=1
        return rt-lt-1
    
    
    for i in range(len(s)):
        len1 = find1(i,i)
        len2 = find2(i,i+1)

        c = max(len1, len2)
        answer = max(answer, c)
    
    return answer