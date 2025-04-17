from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    candidates = []

    for i in range(1, col + 1):
        for comb in combinations(range(col),i):
            tmp = [tuple([item[c] for c in comb]) for item in relation]
            if len(set(tmp)) == row:
                flag= True
                for c in candidates:
                    if set(c).issubset(set(comb)):
                        flag = False
                        break
                if flag:
                    candidates.append(comb)
                        
                
                    
    return len(candidates)
