def solution(numbers, target):
    answer = 0
    
    def dfs(L, target_sum):
        nonlocal answer
        if L == len(numbers):
            if target_sum == target:
                answer += 1
            return
        
        dfs(L+1, target_sum + numbers[L])
        dfs(L+1, target_sum - numbers[L])
        
    dfs(0,0)
    return answer