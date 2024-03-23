def solution(n, t, m, p):
    answer = ''
    
    def convert(number, a):
        if number == 0:
            return '0'
        numbers = "0123456789ABCDEF"
        tmp = ""
        
        while number> 0:
            number, mod = divmod(number,n)
            tmp += numbers[mod]
        return tmp[::-1]
    
    cur = p-1
    game = ''
    for num in range(t*m):
        game += convert(num, n)
    
    while True:
        if len(answer) == t:
            break
            
        answer += game[cur]
        cur += m
        
    return answer
