import heapq
def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    for i in range(0, len(numbers)):
        while stack and stack[-1][1] < numbers[i]:
            id, now= stack.pop()
            answer[id] = numbers[i]
        stack.append((i, numbers[i]))
    
    while stack:
        id,now = stack.pop()
        answer[id] = -1
    return answer