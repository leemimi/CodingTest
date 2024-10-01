def solution(word):
    answer = 0
    dict = []
    
    alp = 'AEIOU'
    def dfs(w,dict):
        if len(w) == 5:
            return
        for a in alp:
            w.append(a)
            dict.append(''.join(w))
            dfs(w, dict)
            w.pop()
    
    words = []
    dit = []
    dfs(words, dit)
        
    return dit.index(word)+1