from collections import deque
def solution(skill, skill_trees):
    answer = 0
    
    arr = list(skill)
    
    for skill in skill_trees:
        flag = True
        q = deque()
        for i in range(len(skill)):
            if skill[i] in arr:
                q.append(skill[i])
        t=0       
        while q:
            if arr[t] != q.popleft():
                flag = False
                break
            
            t+=1
                
        if flag:
            answer+=1
            
            
                
    
    return answer