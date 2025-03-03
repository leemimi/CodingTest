def solution(tickets):
    answer = []
    

    
    def dfs(L, now, ans):
        if L == len(tickets):
            answer.append(ans)
            return
        
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == now:
                visited[i] = 1
                dfs(L+1, tickets[i][1], ans + " "+ tickets[i][1])
                visited[i] = 0
        
    visited = [0]*len(tickets)
    dfs(0,"ICN", "ICN")
        
    answer.sort()

    
    return answer[0].split(" ")