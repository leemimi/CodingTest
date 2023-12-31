from collections import Counter
def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    
    s1=[]
    s2=[]
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s2.append(str2[i]+str2[i+1])
        
    s1 = Counter(s1)
    s2 = Counter(s2)
    
    inner = list((s1&s2).elements())
    union = list((s1|s2).elements())
    
    if len(union) == 0 and len(inner) == 0:
        return 65536
    else:
        return int(len(inner)/len(union)*65536)
    
    return answer