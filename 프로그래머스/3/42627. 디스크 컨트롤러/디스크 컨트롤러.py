import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    num = len(jobs)
    heap = []
    start = -1
    now = 0 #현재시각
    i = 0
    while i<num:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1],job[0]]) #걸리는시간, 시작시간
        if len(heap)>0:
            work = heapq.heappop(heap)
            start = now
            now += work[0] #걸리는 시간 더해주기
            answer += now - work[1]
            i+=1
        else:
            now+=1
    
    
    return answer//num