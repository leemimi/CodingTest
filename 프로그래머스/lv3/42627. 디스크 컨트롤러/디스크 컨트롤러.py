import heapq
def solution(jobs):
    answer = 0
    #힙에 원소가 있다면 바로 진행 대신 소요시간이 적은거 먼저
    
    jobs.sort()
    count, last = 0, -1
    wait = []
    time = jobs[0][0] #현재시간
    length = len(jobs)
    
    while count<length:
        for s,t in jobs:
            if last<s<=time:
                heapq.heappush(wait,(t,s))
        if len(wait)>0:
            last = time
            term, start = heapq.heappop(wait)
            count +=1
            time += term
            answer += time - start
        else:
            time +=1
            
    return answer//length