from itertools import combinations
def solution(n, q, ans):
    answer = 0
    
    f = list(combinations(range(1,n+1),5))
    
    for code in f:
        flag= True
        for i in range(len(q)):
            if len(set(code) & set(q[i])) != ans[i]:
                flag = False
                break
        if flag:

            answer+=1
        
    
    return answer