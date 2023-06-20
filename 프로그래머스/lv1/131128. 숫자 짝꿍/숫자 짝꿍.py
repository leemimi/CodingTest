def solution(X, Y):
    answer = []
    
    xdict = dict()
    ydict = dict()
    
    for x in X:
        xdict[x] = xdict.get(x,0)+1
        
    for y in Y:
        ydict[y] = ydict.get(y,0)+1
        
    for k,y in xdict.items():
        if k in ydict.keys():
            while ydict[k]>0 and xdict[k]>0:
                answer.append(k)
                ydict[k]=ydict.get(k)-1
                xdict[k]=xdict.get(k)-1
    
    if len(answer) <1 : return "-1"
    if (answer.count("0")==len(answer)): return "0"
    
    answer.sort(reverse=True)
    
    return ''.join(answer)