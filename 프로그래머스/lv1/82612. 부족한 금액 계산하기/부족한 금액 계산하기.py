def solution(price, money, count):
    answer = -1
    cnt = 0
    for i in range(1,count+1):
        cnt += (price*i)
    
    answer = money - cnt
    answer = abs(answer) if answer<0 else 0
    return answer