def solution(number, limit, power):
    answer = 0
    
    dp = [0]*(number+1)
    
    for i in range(1,number+1):
        for j in range(1,int(i**(1/2))+1):
            if i%j == 0:
                dp[i] +=1
                if j < i//j:
                    dp[i] +=1
        if dp[i] > limit:
            dp[i] = power
        answer += dp[i]
    
    
    return answer