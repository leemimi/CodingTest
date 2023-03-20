def solution(a, b):
    answer = 1234567890
    arr = [x*y for x,y in zip(a,b)]
    answer = sum(arr)
    return answer