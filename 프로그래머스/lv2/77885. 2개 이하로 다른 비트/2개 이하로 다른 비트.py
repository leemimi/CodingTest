def find(s):
    s = list(s)
    for i in range(len(s)-1,-1,-1):
        if s[i] == '0':
            s[i] = '1'
            if len(s) > i+1:
                s[i+1] = "0"
            break
    return ''.join(s)

def solution(numbers):
    answer = []
    
    for n in numbers:
        if n%2 == 0:
            answer.append(n+1)
        else:
            tmp = "0"+bin(n)[2:]
            answer.append(int(find(tmp),2))
            
    return answer