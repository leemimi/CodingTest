def solution(quiz):
    answer = []
    for q in quiz:
        a = q.split(" ")
        if a[1] == '-':
            ans = int(a[0]) - int(a[2])
        elif a[1] == '+':
            ans = int(a[0]) + int(a[2])
        if ans == int(a[-1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer