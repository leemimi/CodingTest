def solution(storey):
    answer = 1000000001
    k = len(str(storey))+1
    
    def dfs(n,k,cnt):
        nonlocal answer
        
        if not k:
            answer = min(answer,cnt)
            return
        q,r = n//10, n%10
        dfs(q,k-1,cnt+r)
        dfs(q+1,k-1,cnt+10-r)
    
    dfs(storey,k,0)
    
    return answer



