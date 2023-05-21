def solution(record):
    answer = []
    
    word = ["Enter","Leave","Change"]
    reword = ["님이 들어왔습니다.","님이 나갔습니다."]
    
    records = []
    for s in record:
        records.append(s.split(','))
    a=[]
    for w in records:
        a.append(w[0].split())
            
    myid=dict()
    for i in a:
        if i[1] not in myid and i[0]==word[0]:
            myid[i[1]]=i[2]
        if i[0] == word[2] :
            myid[i[1]] = i[2]
        if i[1] in myid and i[0] == word[0]:
            myid[i[1]] = i[2]
            
    for i in a:
        if i[0] == word[0]:
            answer.append(myid[i[1]]+reword[0])
        elif i[0] == word[1]:
            answer.append(myid[i[1]]+reword[1])
            
        
    
    
    return answer