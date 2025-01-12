def solution(user_id, banned_id):
    answer = 0
    
    idx=[ [] for _ in range(len(banned_id)) ]
    for u in range(len(user_id)):
        user_id[u] = list(user_id[u])
    
    for b in range(len(banned_id)):
        banned_id[b]=list(banned_id[b])
        for i in range(len(banned_id[b])):
            if banned_id[b][i] == '*':
                idx[b].append(i)
                
    def dfs(L, tmp):
        if L == len(banned_id):
            ans.append(tmp)
            tmp = []
            return
        for u in range(len(user_id)):
            if len(user_id[u])==len(banned_id[L]):
                ban = banned_id[L][:]
                for i in idx[L]:
                    ban[i] = user_id[u][i]
                    
                if visited[u]==0 and user_id[u] == ban:
                    visited[u] = 1
                    dfs(L+1, tmp+["".join(user_id[u])])
                    visited[u] = 0
                
        
    visited=[0]*len(user_id)    
    ans = []
    dfs(0,[])
    answer = set()
    for a in ans:
        answer.add(tuple(set(sorted(a))))
    
    return len(answer)