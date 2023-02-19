def solution(array, n):
    answer = 0
    min = 2147000000
    for i in array:
        if abs(n-i) < min:
            min = abs(n-i)
            answer = i
        if abs(n-i) == min:
            if answer < i:
                continue
            else:
                answer = i
                min = abs(n-i)
    return answer