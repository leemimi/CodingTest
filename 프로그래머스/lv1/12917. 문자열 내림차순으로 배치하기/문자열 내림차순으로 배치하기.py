def solution(s):
    answer = ''
    slist = list(map(lambda x: str(x),s))
    slist.sort(reverse=True)
    for i in slist:
        if(i.islower()):
            answer+=i
    
    for i in slist:
        if(i.isupper()):
            answer+=i
    return answer