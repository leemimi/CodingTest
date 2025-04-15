def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    
    def dfs(n,computers,idx, visited):
        visited[idx] = True
        
        for j in range(n):
            if j!=idx and computers[idx][j] == 1:
                if visited[j] == False:
                    dfs(n,computers,j,visited)
        
    
    for i in range(n):
        if visited[i] == False:
            dfs(n,computers,i,visited)
            answer +=1
    
    
    return answer