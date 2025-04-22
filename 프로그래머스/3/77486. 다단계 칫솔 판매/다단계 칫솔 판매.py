def solution(enroll, referral, seller, amount):
    answer = []
    dict = {}
    money = {}
    for i in range(len(referral)):
        dict[enroll[i]] = referral[i]
        money[enroll[i]] = 0
    sell = []
    for i in range(len(seller)):
        sell.append((seller[i], amount[i]*100))
    
    for s in sell:
        money[s[0]] += int(s[1]*0.9)
        e = int(s[1]*0.1)
        mom = dict[s[0]]
        
        while "-"!= mom:
            if e*0.1 < 1:
                money[mom]+= e
                break
            money[mom] += e - int(e*0.1)
            e = int(e*0.1)
            mom = dict[mom]
        
    for k in enroll:
        answer.append(money[k])
            
    return answer