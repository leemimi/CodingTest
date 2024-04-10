from collections import defaultdict
def solution(user_id, banned_id):
    answer = []
    
    res = [[]]
    for banned in banned_id:
        ban = []
        for u in user_id:

            if len(u) != len(banned):
                continue
            flag = True
            for i in range(len(u)):
            
                if banned[i] == '*':
                    continue
                if banned[i] != '*' and banned[i]!= u[i]:
                    flag = False
                    break
            if flag:
                for r in res:
                    if u not in r:
                        ban.append(r+[u])
        res = ban
    for r in res:
        if set(r) not in answer:
            answer.append(set(r))
    
    # print(answer)
        
    return len(answer)