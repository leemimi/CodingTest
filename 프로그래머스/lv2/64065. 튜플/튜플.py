def solution(s):
    answer = []
    
    s=s[2:-2].split("},{")
    
    s = sorted(s, key=lambda x: len(x))
    
    for item in s:
        item = list(map(int, item.split(",")))
        for i in item:
            if i not in answer:
                answer.append(i)
    return answer