from collections import deque
def bfs(destination, arr, costs):
    q = deque([destination])
    costs[destination] = 0

    while q:
        x= q.popleft()
        for i in arr[x]:
            if costs[i] == -1:
                q.append(i)
                costs[i] = costs[x]+1
    return costs

def solution(n, roads, sources, destination):
    answer = []
    arr = [ [] for _ in range(n+1)]
    
    for s,e in roads:
        arr[s].append(e)
        arr[e].append(s)

    costs = [-1]*(n+1)
    
    costs = bfs(destination, arr, costs)
    
        
    return [costs[s] for s in sources]
