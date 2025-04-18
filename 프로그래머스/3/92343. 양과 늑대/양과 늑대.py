from collections import defaultdict
def solution(info, edges):
    answer = 0
    
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
    
    
    def dfs(sheep, wolf, now, possible):
        nonlocal answer
        answer = max(sheep, answer)
        
        if sheep <= wolf:
            return
        
        for next in possible:
            new = possible.copy()
            new.remove(next)
            new.extend(graph[next])
            new_sheep = sheep
            new_wolf = wolf
            if info[next] == 0:
                new_sheep+=1
            else:
                new_wolf +=1
            dfs(new_sheep,new_wolf,next, new)
            
        
    
    dfs(1,0,0,graph[0])
    
    
    
    return answer