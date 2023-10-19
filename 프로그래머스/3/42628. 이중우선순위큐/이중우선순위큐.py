import heapq
def solution(operations):
    heap =[]
    
    
    for nums in operations:
        if len(heap) > 0 and nums == 'D 1':
            heap = heapq.nlargest(len(heap), heap)[1:]
            heapq.heapify(heap)
        elif len(heap) > 0 and nums == 'D -1':
            heapq.heappop(heap)
        else:
            a,b = nums.split(" ")
            if a == 'I':
                heapq.heappush(heap, int(b))
        print(heap)
    
    if len(heap)<1:
        return [0,0]
    else:
        return [max(heap),min(heap)]
    