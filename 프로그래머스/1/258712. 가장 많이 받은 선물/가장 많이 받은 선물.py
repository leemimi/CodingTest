def solution(friends, gifts):
    answer = 0
    gift = {}
    gidx = {}
    for f in friends:
        gift[f] = {}
        gidx[f] = 0
        
    
    for g in gifts:
        a,b = g.split(" ")
        if b in gift[a]:
            gift[a][b] +=1
        else:
            gift[a][b] = 1
        gidx[a] +=1
        gidx[b] -=1
    
    print(gift)
    
    get_gift = [0 for _ in friends]
    for i in range(len(friends)):
        friend = friends[i]
        for j in range(i+1,len(friends)):
            another = friends[j]
            a = gift[friend][another] if another in gift[friend] else 0
            b = gift[another][friend] if friend in gift[another] else 0
            
            if a > b:
                get_gift[i] +=1
            elif a<b:
                get_gift[j] +=1
            elif a ==b:
                ai,bi = gidx[friend], gidx[another]
                if ai>bi:
                    get_gift[i] +=1
                elif ai<bi:
                    get_gift[j] +=1
    answer = max(get_gift)
    
    return answer