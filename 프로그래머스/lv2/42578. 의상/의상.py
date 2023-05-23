def solution(clothes):
    ans = 1
    
    clothe = {}
    
    for i in clothes:
        clothe[i[-1]] = 0
    
    for k in clothes:
        clothe[k[-1]]+=len(k[:-1])
    
        
    for h in clothe.values():
        ans *= h+1

    return ans-1