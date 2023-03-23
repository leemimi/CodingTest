def solution(t, p):
    answer = 0
    
    l=[]
    for i in range(len(t)):
        l.append(t[i:len(p)+i])
        if(len(p)+i==len(t)):break
    
    l = list(map(int,l))
    
    p = int(p)
    for num in l:
        if(num<=p):
            answer+=1
    
    return answer