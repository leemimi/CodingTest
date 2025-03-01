import heapq
def solution(players, m, k):
    answer = 0
    
    q = []
    #현재 서버
    now_server = 0
    for i in range(24):

        while q and q[0][0] == i:
            now_server -= heapq.heappop(q)[1]
           
        need_server = players[i]//m
        tmp = now_server - need_server
        
        if(tmp<0):
            tmp = -tmp
            now_server += tmp
            answer += tmp
            heapq.heappush(q, (i+k,tmp))
    return answer