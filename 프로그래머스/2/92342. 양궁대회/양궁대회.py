def solution(n, info):
    global maxDiff, answer
    answer = [-1]
    tmp = [0]*11
    maxDiff = 0
    
    def find_gap(score):
        
        apich, rian = 0, 0
        for i in range(len(score)):
            if score[i] > 0 or info[i] > 0:
                if score[i] > info[i]:
                    rian += (10 - i)
                else:
                    apich += (10-i)
        return (rian>apich, abs(rian- apich))
    
    
    def dfs(L, cnt):
        global maxDiff, answer
        if L == 11 or cnt ==0:
            winner, gap = find_gap(tmp)
            
            if winner:
                if cnt >= 0:
                    tmp[10] = cnt
                if gap > maxDiff:
                    maxDiff = gap
                    answer = tmp.copy()

                    
                elif gap == maxDiff:
                    for i in range(len(tmp)):
                        if answer[i] > 0:
                            a = i
                        if tmp[i] > 0 :
                            b = i
                    if b > a :
                        answer = tmp.copy()
                        
            return
            

        if cnt >info[L]:
            tmp[L] = info[L]+1
            dfs(L+1, cnt - (info[L]+1))
            tmp[L] = 0
        
        dfs(L+1, cnt)
    

    dfs(0,n)
    return answer