import heapq
def solution(operations):
    answer = [0,0]
    
    maxh = []
    minh = []
    for oper in operations:
        p, num = oper.split()
        num = int(num)
        if p == 'I':
            heapq.heappush(maxh, -num)
            heapq.heappush(minh, num)
        elif p == 'D':
            if not maxh:
                continue
            elif num == 1:
                minh.remove(-heapq.heappop(maxh))
            else:
                maxh.remove(-heapq.heappop(minh))

    max_num = min_num = 0
    if maxh:
        max_num = -heapq.heappop(maxh)
    if minh:
        min_num = heapq.heappop(minh)
    answer = [max_num, min_num]
    return answer