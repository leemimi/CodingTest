import math
def solution(fees, records):
    answer = []
    
    dict ={}
    end = 23*60 + 59
    
    def calc(tmp, fees):
        m = fees[1]
        if tmp <= fees[0]:
            return m
        else:
            v = abs(tmp - fees[0])
            m += math.ceil(v/fees[2])*fees[3]
        return m
    
    
    for record in records:
        r = record.split(' ')
        r[1] = int(r[1])
        r[0] = int(r[0][0:2])*60 + int(r[0][3:5])
        if r[1] not in dict:
            dict[r[1]] = [(r[0], r[2])]
        else:
            dict[r[1]].append((r[0],r[2]))
            
    ans = {}
    #r[0]번호, 뒤가 인 아웃
    for key, record in dict.items():
        money = 0
        time = 0
        flag = True
        count = 0
        for r in record:
            if r[1] == 'IN':
                flag = True
                time = r[0]
            else:
                flag = False
                tmp = abs(time - r[0])
                count += tmp
        
        if flag:
            tmp = abs(end - time)
            count += tmp
            print(key, count)
            money = calc(count, fees)
        else:
            money = calc(count, fees)
            
        
        ans[key] = round(money)
        
    ans = sorted(ans.items(), key=lambda x:x[0])
    
    for k,v in ans:
        answer.append(v)
        
    
    return answer