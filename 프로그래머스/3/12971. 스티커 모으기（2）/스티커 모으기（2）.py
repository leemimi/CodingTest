def solution(sticker):
    answer = 0
    
    if len(sticker) ==1:
        return sticker[0]
    elif len(sticker) ==2:
        return max(sticker)
    
    dp1 = [0]*(len(sticker)+1)
    dp2 = [0]*(len(sticker)+1)
    
    dp1[1] = sticker[0]
    dp2[1] = 0
    
    for i in range(2,len(sticker)):
        dp1[i] += max(sticker[i-1]+dp1[i-2], dp1[i-1])
        
    for i in range(2,len(sticker)+1):
        dp2[i] += max(sticker[i-1]+dp2[i-2], dp2[i-1])
    

    
    return max(dp1[-2],dp2[-1])