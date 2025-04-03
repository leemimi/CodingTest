import heapq
def solution(A, B):
    answer = 0
    n = len(A)
    heapq.heapify(A)
    heapq.heapify(B)

    for i in range(n):
        anum = heapq.heappop(A)
        bnum = heapq.heappop(B)
        
        if anum < bnum:
            answer+=1
        else:
            heapq.heappush(A, anum)
        
    return answer