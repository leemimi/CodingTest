def solution(players, callings):
    answer = []
    
    p = {player:i for i, player in enumerate(players)} #선수:등수
    core = {i:player for i, player in enumerate(players)} #등수: 선수
    
    for i in callings:
        loc = p[i]
        loc2 = loc -1
        i2 = core[loc2]
        
        core[loc] = i2
        core[loc2] = i
        
        p[i] = loc2
        p[i2] = loc
        
    
    return list(core.values())