def solution(s, skip, index):
    answer=''
    alpha = [ chr(i) for i in range(97,123)]
    
    for i in skip:
        if i in alpha:
            alpha.remove(i)
    
    for k in s:
        j=(alpha.index(k)+index)%len(alpha)
        answer+=alpha[j]
    
    return answer