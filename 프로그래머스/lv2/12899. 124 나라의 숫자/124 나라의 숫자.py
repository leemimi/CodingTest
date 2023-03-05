def solution(n):
    answer = ''
    numbers = "4","1","2"
    while(n>0):
        answer += numbers[n%3]
        if(n%3==0): n=n-1
        n=n//3
        
    return answer[::-1]