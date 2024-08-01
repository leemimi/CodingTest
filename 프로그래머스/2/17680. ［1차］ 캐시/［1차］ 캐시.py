from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    cities = deque(cities)
    q = []
    time = 0

    while cities:
        if cacheSize == 0:
            time += 5*len(cities)
            break
        c = cities.popleft()
        c = c.lower()
        if c not in q:
            if len(q) == cacheSize:
                q.pop(0)
            q.append(c)
            time += 5
        else:
            q.pop(q.index(c))
            q.append(c)
            time+=1
                
    
    return time