def solution(s):
    answer = []
    words = s.split(' ')
    
    for word in words:
        if word:
            word = word[:1].upper() + word[1:].lower()
            answer.append(word)
        else:
            answer.append(word)
            
    
    return ' '.join(answer)