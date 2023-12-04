import math
def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        y_max = math.floor(math.sqrt(r2**2 - i**2))
        x_max = 0 if i>=r1 else math.ceil(math.sqrt(abs(r1**2 - i**2)))
        answer += y_max - x_max + 1
    return answer*4