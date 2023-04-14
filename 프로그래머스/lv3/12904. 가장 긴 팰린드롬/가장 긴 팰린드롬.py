def solution(s):
    answer = 0
    
    if s == s[::-1]:
        return len(s)
    
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            re = s[i:j]
            if re == re[::-1] :
                answer = max(answer, len(re))
    
    return answer