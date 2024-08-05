def solution(word):
    answer = 0
    dict ='AEIOU'
    idx = 0
    
    def dfs(L, s):
        nonlocal idx
        nonlocal answer
        if s == word:
            answer = idx
            return
        
        if L > 5:
            return
        
        idx+=1
        for i in range(5):
            dfs(L+1, s+dict[i])


    i = dfs(0,'')
    return answer