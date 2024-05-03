import heapq
def solution(N, road, K):
    answer = 0
    distance = [1e9]*(N+1)
    arr = [[] for _ in range(N+1)]
    
    for a,b,c in road:
        arr[a].append((b,c))
        arr[b].append((a,c))
    
    distance[1] = 0
    h = [(0,1)]
    
    while h:
        dis, node = heapq.heappop(h)
        
        if distance[node]<dis:
            continue
        
        for nn, nd in arr[node]:
            d = dis + nd
            if distance[nn] > d:
                distance[nn] = d
                heapq.heappush(h,(d,nn))
    for d in distance[1:]:
        if d<=K:
            answer+=1
    
    return answer