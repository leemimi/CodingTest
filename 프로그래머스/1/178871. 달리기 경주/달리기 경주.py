from collections import defaultdict
def solution(players, callings):
    answer = []
    
    dict = {}
    
    for i in range(len(players)):
        dict[players[i]] = i
        
    for i in callings:
        win = dict[i] -1
        lose = dict[i]
        
        players[win], players[lose] = players[lose], players[win]
        dict[players[win]],dict[players[lose]] = win, lose
        
        

    
    
    return players