from itertools import combinations
def solution(orders, course):
    answer = []
    
    for c in course:
        arr = []
        dict = {}
        for o in orders:
            arr = list(combinations(sorted(o),c))
            
            for a in arr:
                a = ''.join(a)
                
                if a in dict:
                    dict[a] +=1
                else:
                    dict[a] = 1
        max_order = [k for k,v in dict.items() if ((v == max(dict.values())) and v >= 2)]
        answer.extend(max_order)
    answer.sort()
    
    return answer