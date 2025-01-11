import heapq
def solution(n, works):
    answer = 0
    
    q = []
    if n >= sum(works):
        return 0

    works = [-i for i in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i +=1
        heapq.heappush(works, i)
    
    answer = sum([w**2 for w in works])
    
    return answer