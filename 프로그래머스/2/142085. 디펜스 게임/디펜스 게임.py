import heapq
def solution(n, k, enemy):
    answer = 0
    
    if k >= len(enemy) :
        return len(enemy)
    
    use = []
    
    for i in range(len(enemy)):
        if k>0:
            k-=1
            answer +=1
            heapq.heappush(use, enemy[i])
        else:
            heapq.heappush(use,enemy[i])
            n -= heapq.heappop(use)
            if n<0:
                break
            else:
                answer+=1
    return answer