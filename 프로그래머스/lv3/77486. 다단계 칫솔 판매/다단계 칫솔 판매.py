def find(parent, money, number,answer):
    if parent[number] == number or money//10 == 0:
        answer[number] += money
        return
    send = money//10
    mine = money- send
    answer[number] +=mine
    find(parent,send,parent[number], answer)
    return

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0]*(n+1)
    d = {} #이름-번호
    parent = [i for i in range(n+1)]
    
    #이름-번호 저장
    for i in range(n):
        d[enroll[i]] = i+1
    
    for i in range(n):
        if referral[i] == '-':
            parent[i+1] = 0
        else:
            parent[i+1] = d[referral[i]]
    
    for i in range(len(seller)):
        find(parent, amount[i]*100, d[seller[i]], answer)
    
    return answer[1:]