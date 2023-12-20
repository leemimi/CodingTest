from math import ceil
def solution(fees, records):
    answer = []
    
    def contime(times):
        times = times.split(':')
        return int(times[0])*60 + int(times[1])
    maxtime = 23*60 + 59
    res = {}
    for record in records:
        time, num, io = record.split()
        time = contime(time)
        if num in res:
            res[num].append([time,io])
        else:
            res[num] = [[time,io]]
    
    ans = {}
    for r in res:
        
        total = 0
        pay = fees[1]
        
        if len(res[r]) %2 != 0:
            res[r].append([maxtime,'OUT'])
        
        for m in res[r]:
            if m[1] == 'IN':
                total -= m[0]
            else:
                total += m[0]
        if total > fees[0]:
            pay += ceil((total - fees[0])/fees[2])*fees[3]
        
        ans[r] = pay
    ans = sorted(ans.items())
    

    return [b for a,b in ans]