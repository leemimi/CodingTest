def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    
    dict = {}
    time = {}
    for id in id_list:
        dict[id] =[]
        time[id] = 0
    for re in report:
        a,b = re.split(" ")
        if b not in dict[a]:
            dict[a].append((b))
            time[b] +=1
        
    ban = set()
    for key, val in time.items():
        if val>=k:
            ban.add(key)
            
    for i in range(len(id_list)):
        now = id_list[i]
        for name in dict[now]:
            if name in ban:
                answer[i] +=1
    print(answer)
    
            
    return answer