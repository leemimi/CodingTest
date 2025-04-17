from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
        

    visited = [-1]*(n+1)
    visited[destination] = 0
    q = deque()
    q.append(destination)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[now] +1
    
    for s in sources:
        answer.append(visited[s])
    

        
        
    return answer