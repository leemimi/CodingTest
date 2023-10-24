from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    
    dict = {}
    i=0
    for w in want:
        dict[w] = number[i]
        i+=1
    

    for i in range(len(discount)-9):
        tmp = dict.copy()
        for j in range(i,i+10):
            if discount[j] in tmp and tmp[discount[j]] !=0:
                tmp[discount[j]]-=1
            else:
                break
        if sum(tmp.values()) == 0:
            answer +=1

    return answer