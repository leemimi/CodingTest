from collections import Counter
def solution(str1, str2):
    answer = 0
    
    a = []
    b = []
    
    for i in range(0,len(str1)-1):
        s1 = str1[i] + str1[i+1]
        if not str1[i+1].isalpha() or not str1[i].isalpha():
            continue
        s1 = s1.upper() 
        a.append(s1)

    for i in range(0,len(str2)-1):
        s2 = str2[i] + str2[i+1]
        if not str2[i+1].isalpha() or not str2[i].isalpha():
            continue
        s2 = s2.upper()
        b.append(s2)
        
    ca = Counter(a)
    cb = Counter(b)
    
    ja = ca&cb
    jb = ca|cb
    
    print(ja)
    print(jb)
    
    ja = sum(ja.values())
    jb = sum(jb.values())


    if(jb == 0):
         return 65536
    
    answer = ja/jb
    
    return int(answer*65536)