def solution(seoul):
    answer = ''
    for i, key in enumerate(seoul):
        if key == "Kim":
            answer = f"김서방은 {i}에 있다"
    return answer