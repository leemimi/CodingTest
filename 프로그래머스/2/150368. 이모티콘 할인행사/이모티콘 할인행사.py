from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    data = [10, 20, 30, 40]
    
    discount = []
    def dfs(L,tmp):
        if L == len(tmp):
            discount.append(tmp[:])
            return
        else:
            for i in data:
                tmp[L]+=i
                dfs(L+1,tmp)
                tmp[L]-=i
    dfs(0,[0]*len(emoticons))
    
    for dis in discount:
        cnt = 0
        get = 0
        for u in users:
            pay = 0
            for j in range(len(dis)):
                if u[0] <= dis[j]:
                    pay += emoticons[j]*(100-dis[j])/100
            if pay >= u[1]:
                pay = 0
                cnt += 1
            get += pay
        if cnt >= answer[0]:
            if answer[0] == cnt:
                answer[1] = max(answer[1], get)
            else:
                answer[1] = get
            answer[0] = cnt
            
            
                
    
    return answer