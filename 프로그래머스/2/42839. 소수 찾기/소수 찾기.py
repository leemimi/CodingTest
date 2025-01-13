import math
def solution(numbers):
    answer = 0
    
    visited = [False]*len(numbers)
    ans = set()
    def check(tmp):
        tmp = int(tmp)
        if tmp <2 :
            return False
        for j in range(2, int(math.sqrt(tmp))+1):
            if tmp%j ==0:
                return False
        return True
    
    def dfs(L, tmp):
        nonlocal answer
        if L == len(numbers):
            if tmp == '':
                return
            if int(tmp) in ans:
                return
            if check(tmp):
                ans.add(int(tmp))
                answer +=1
            return
        
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(L+1, tmp)
                dfs(L+1, tmp+numbers[i])
                visited[i] = False
        
        
    dfs(0,'')
    return answer