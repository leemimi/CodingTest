def solution(n, info):
    global max_gap, answer
    answer = [-1]
    score =[0]*11
    max_gap = 0
    
    
    def is_winner_gap(score):
        a=0
        b=0
        
        for i in range(len(info)):
            if info[i] >0 or score[i]>0:
                if info[i]>= score[i]:
                    a+=(10-i)
                else:
                    b+=(10-i)
        return (b>a, abs(a-b))
        
    
    
    def dfs(L,cnt):
        global answer, max_gap
        if L == 11 or cnt ==0:
            is_winner, gap = is_winner_gap(score)
            
            if is_winner:
                if cnt>=0:
                    score[10] = cnt
                    
                if gap> max_gap:
                    max_gap = gap
                    answer= score.copy()
                elif gap == max_gap:
                    for i in range(len(score)):
                        if answer[i]>0:
                            ans_i = i
                        if score[i] >0:
                            score_i = i
                    if ans_i < score_i:
                        answer=score.copy()
            return
        
        if cnt>info[L]:
            score[L] = info[L]+1
            dfs(L+1, cnt-(info[L]+1))
            score[L] = 0
            
        dfs(L+1,cnt)
                
    
    dfs(0,n)
    
    return answer