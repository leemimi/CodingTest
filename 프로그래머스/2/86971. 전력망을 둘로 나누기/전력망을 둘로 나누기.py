from collections import deque
def solution(n, wires):
    answer = n+1
    arr = [[] for _ in range(n+1)]
    
    def bfs(start):
        q = deque([start])
        visited = [0]*(n+1)
        visited[start] = 1
        cnt = 1
        while q:
            s = q.popleft()
            
            for i in arr[s]:
                if visited[i] != 1:
                    visited[i] = 1
                    q.append(i)
                    cnt +=1
        return cnt
        
    
    for a,b in wires:
        arr[a].append(b)
        arr[b].append(a)
    
    for a,b in wires:
        arr[a].remove(b)
        arr[b].remove(a)
        
        answer = min(abs(bfs(a) - bfs(b)),answer)
        
        arr[a].append(b)
        arr[b].append(a)
    
    
    return answer