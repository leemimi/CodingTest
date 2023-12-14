def solution(s):
    answer = []
    dict = {}
    s = s.replace("{","").replace("}","").split(",")
    
    for r in s:
        r = int(r)
        if r not in dict:
            dict[r] = 1
        else:
            dict[r] +=1
    answer = sorted(dict, key= lambda x:dict[x], reverse= True)
        
    
    return answer