import heapq
def solution(A, B):
    answer = 0
    
    A.sort() #1 3 5 7
    B.sort()
    heapq.heapify(B)
    heapq.heapify(A)
    
    while B and A:
        b = heapq.heappop(B)
        a = heapq.heappop(A)
        if(a<b):
            answer+=1
        else:
            heapq.heappush(A,a)

    

        
    return answer