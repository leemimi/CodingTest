def solution(a, b):
    answer = ''
    weekend = ["FRI","SAT","SUN","MON","TUE", "WED", "THU"]
    month ={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    
    sum = 0
    day = 0
    cnt = 0
    for v in month.values():
        if(cnt == a-1):
            break
        else:
            sum+=v
            cnt+=1
    day = (sum+b)%7
    answer = weekend[day-1]
    return answer