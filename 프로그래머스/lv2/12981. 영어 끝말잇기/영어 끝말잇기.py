def solution(n, words):
    answer = [0,0]

    idx = 0
    for i in range(1,len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            answer[0] = i%n +1 
            if answer[0] == 0 :
                answer[0] = n
            answer[1] = i//n+1
            break
    return answer