def solution(skill, skill_trees):
    answer = 0
    
    for i in range(len(skill_trees)):
        possible = True
        tmp = ''
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                if j < skill.index(skill_trees[i][j]):
                    possible = False
                    break
                else:
                    tmp += skill_trees[i][j]
                    
        if possible and tmp == skill[:len(tmp)]:        
            answer+=1
            
            
            
            
            
    return answer