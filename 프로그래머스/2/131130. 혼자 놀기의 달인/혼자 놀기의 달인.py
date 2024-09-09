def solution(cards):
    answer = 0
    arr =[]
    def dfs(num, cnt):
        if visited[num-1]:
            arr.append(cnt)
            return
        
        visited[num-1] = True
        dfs(cards[num-1],cnt+1)
        
    
    visited=[False]*len(cards)
    
    for i in range(len(cards)):
        if not visited[i]:
            visited[i] = True
            dfs(cards[i],1)
    
    
    if len(arr)>=2:
        arr.sort()
        answer = arr[-1]*arr[-2]
    
    
    return answer