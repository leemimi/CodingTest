from collections import deque
def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        flag = True
        tmp =''
        for j in range(len(tree)):
            if tree[j] in skill:
                if j < skill.index(tree[j]):
                    flag = False
                    break
                else:
                    tmp += tree[j]
                    
        if flag and tmp == skill[:len(tmp)]:
            answer+=1
                    
    
    return answer