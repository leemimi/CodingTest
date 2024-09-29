from collections import deque
def solution(n, t, m, timetable):
    answer = 0
    start = 60*9
    end = 23*60 + 59
    
            
    def calc(a,b):
        return int(a)*60 + int(b)
    
    def re_calc(c):
        ah = str(c//60)
        am = str(c%60)
        if len(ah) == 1:
            ah = '0'+ah
        if len(am) == 1:
            am = '0'+ am
        tmp = ah+':'+am
        return tmp
    
    for i in range(len(timetable)):
        timetable[i] = calc(timetable[i][0:2], timetable[i][3:5])
        
    timetable.sort()
    q = deque(timetable)
    
    for _ in range(n):
        mx = m
        last = start
        while q:
            if mx!=0 and q[0] <= start:
                last = q.popleft()
                mx-=1
            else:
                break
        if _== n-1 and mx==0:
            answer = last -1
        elif _==n-1 and mx!=0:
            answer = start
                
        start += t       
        
    answer = re_calc(answer)

    return answer