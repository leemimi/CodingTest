def solution(today, terms, privacies):
    answer = []
    dict = {}
    for t in terms:
        tt = t.split(" ")
        dict[tt[0]] = int(tt[1])
    
    day = 28
    
    tyear, tmon, tday = today.split(".")
    tyear = int(tyear)
    tmon = int(tmon)
    tday = int(tday)
    i = 1
    for pri in privacies:
        days, num = pri.split(" ")
        year, month, day = days.split(".")
        year = int(year)
        month = int(month)
        day = int(day)
        month += dict[num]
        if month >12:
            year+=(month-1)//12
            month = (month-1)%12 +1
        day -=1
        if day == 0:
            day = 28
            month -=1
            if month ==0:
                month = 12
                year-=1
        
        
        if(year, month,day)<(tyear, tmon, tday):
            answer.append(i)
            
        i+=1
        
    
    return answer