def solution(record):
    answer = []
    dict = {}
    for i in range(len(record)):
        now = record[i].split(' ')
        
        if now[0] == 'Leave':
            continue
        dict[now[1]] = now[2]

    for r in record:
        now = r.split(' ')
        s = dict[now[1]]
        if now[0] == 'Enter':
            s += '님이 들어왔습니다.'
            answer.append(s)
            
        elif now[0] == 'Leave':
            s += '님이 나갔습니다.'
            answer.append(s)
        
        
    return answer