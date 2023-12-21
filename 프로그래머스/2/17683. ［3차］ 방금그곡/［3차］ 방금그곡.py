def solution(m, musicinfos):
    answer = '(None)'
    m = m.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')
    def run_time(a,b):
        a = a.split(':')
        a = int(a[0])*60 + int(a[1])
        
        b = b.split(':')
        b = int(b[0])*60 + int(b[1])
        return b-a
    max_time = 0
    for info in musicinfos:
        info = info.split(',')
        time = run_time(info[0],info[1])
        
        info[3] = info[3].replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')
            
        info[3] = info[3] * (time // len(info[3])) + info[3][0:time % len(info[3])]

        if m in info[3] and time > max_time:
            max_time = time
            answer = info[2]

    return answer