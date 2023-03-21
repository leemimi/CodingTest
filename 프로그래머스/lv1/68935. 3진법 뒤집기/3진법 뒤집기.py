def solution(n):
    answer = 0
    arr = []
    while n>0:
        arr.append(n%3)
        n = n//3
    j = 0
    for i in reversed(range(len(arr))):
        answer += arr[i]*(3**(j))
        j+=1
    return answer