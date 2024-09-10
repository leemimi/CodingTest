def solution(n, info):
    answer = []
    
    score = [0]*11
    diff = 0
    
    def dfs(m,L):
        nonlocal answer, diff, score
        
        if m == n:
            a,b =0,0
            for j in range(11):
                if score[j] > info[j]:
                    b +=(10-j)
                elif 0!=info[j] and score[j] <= info[j]:
                    a+= (10-j)
            if b>a:
                if diff < abs(b-a):
                    diff = abs(b-a)
                    answer = score[:]
                elif diff == abs(b-a):
                    for i in range(10,-1,-1):
                        if score[i] < answer[i]:
                            break
                        if score[i] > answer[i]:
                            answer = score[:]
                            break
            return
        
        for i in range(L,11):
            score[i] +=1
            dfs(m+1,i)
            score[i]-=1
        
    
        
    dfs(0,0)
    return answer if answer else [-1]