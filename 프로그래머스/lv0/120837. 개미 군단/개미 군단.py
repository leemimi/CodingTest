def solution(hp):
    answer = 0
 
    i =5
    while True:
        if (hp<=0) :break;
        answer += hp//i
        hp = hp%i
        i = i-2
    return answer