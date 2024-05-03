import heapq
def solution(book_time):
    answer = 1
    
    book = [(int(s[:2])*60+int(s[3:]),int(e[:2])*60+int(e[3:])) for s,e in book_time]
    book.sort()
    
    h = []
    
    for s,e in book:
        if not h:
            heapq.heappush(h,e)
            continue
        if h[0]<=s:
            heapq.heappop(h)
        else:
            answer+=1
        heapq.heappush(h,e+10)
    return answer