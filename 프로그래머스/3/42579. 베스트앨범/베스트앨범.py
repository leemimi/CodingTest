from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    gen = {}
    dict = {}
    for i ,(g,p) in enumerate(zip(genres, plays)):
        if g not in gen:
            gen[g] = [(i,p)]
        else:
            gen[g].append((i,p))
        
        if g not in dict:
            dict[g] = p
        else:
            dict[g] +=p
            
    
    
    for (k,v) in sorted(dict.items(), key = lambda x:x[1], reverse = True):
        for (i,p) in sorted(gen[k], key= lambda x:x[1], reverse= True)[:2]:
            answer.append(i)
    
    
    print(gen)
    print(dict)
    return answer