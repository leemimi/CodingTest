import heapq
def solution(N, road, K):
    answer = 0
    
    def dijk(arr, dist):
        heap = []
        heapq.heappush(heap, [1,0])
        while heap:
            node, cost = heapq.heappop(heap)
            for n, c in graph[node]:
                if cost + c < dist[n]:
                    dist[n] = cost+c
                    heapq.heappush(heap, [n,cost+c])
    
    
    graph = [[] for _ in range(N+1)]
    dist = [float('inf')]*(N+1)
    dist[1] = 0
    for r in road:
        graph[r[0]].append((r[1],r[2]))
        graph[r[1]].append((r[0],r[2]))
    dijk(graph, dist)

    for i in dist:
        if i<=K:
            answer+=1
    
    return answer